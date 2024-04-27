from app.tags.models import Tag
from app.config import settings


from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2


async def get_image_tags(image_data):

    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + settings.PAT),)

    user_data_object = resources_pb2.UserAppIDSet(user_id=settings.USER_ID, app_id=settings.APP_ID)

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=user_data_object,
            model_id=settings.MODEL_ID,
            version_id=settings.MODEL_VERSION_ID,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            base64=image_data
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    output = post_model_outputs_response.outputs[0]
    tags = []
    values = []
    for concept in output.data.concepts:
        tags.append(Tag(name=concept.name))
        values.append(concept.value)

    return tags, values
