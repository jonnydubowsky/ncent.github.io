"""Generated client library for vision version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.vision.v1 import vision_v1_messages as messages


class VisionV1(base_api.BaseApiClient):
  """Generated client library for service vision version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://vision.googleapis.com/'

  _PACKAGE = u'vision'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/cloud-vision']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'VisionV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new vision handle."""
    url = url or self.BASE_URL
    super(VisionV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.files = self.FilesService(self)
    self.images = self.ImagesService(self)
    self.locations_operations = self.LocationsOperationsService(self)
    self.locations = self.LocationsService(self)
    self.operations = self.OperationsService(self)

  class FilesService(base_api.BaseApiService):
    """Service class for the files resource."""

    _NAME = u'files'

    def __init__(self, client):
      super(VisionV1.FilesService, self).__init__(client)
      self._upload_configs = {
          }

    def AsyncBatchAnnotate(self, request, global_params=None):
      r"""Run asynchronous image detection and annotation for a list of generic.
files, such as PDF files, which may contain multiple pages and multiple
images per page. Progress and results can be retrieved through the
`google.longrunning.Operations` interface.
`Operation.metadata` contains `OperationMetadata` (metadata).
`Operation.response` contains `AsyncBatchAnnotateFilesResponse` (results).

      Args:
        request: (AsyncBatchAnnotateFilesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('AsyncBatchAnnotate')
      return self._RunMethod(
          config, request, global_params=global_params)

    AsyncBatchAnnotate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'vision.files.asyncBatchAnnotate',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1/files:asyncBatchAnnotate',
        request_field='<request>',
        request_type_name=u'AsyncBatchAnnotateFilesRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ImagesService(base_api.BaseApiService):
    """Service class for the images resource."""

    _NAME = u'images'

    def __init__(self, client):
      super(VisionV1.ImagesService, self).__init__(client)
      self._upload_configs = {
          }

    def Annotate(self, request, global_params=None):
      r"""Run image detection and annotation for a batch of images.

      Args:
        request: (BatchAnnotateImagesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchAnnotateImagesResponse) The response message.
      """
      config = self.GetMethodConfig('Annotate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Annotate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'vision.images.annotate',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path=u'v1/images:annotate',
        request_field='<request>',
        request_type_name=u'BatchAnnotateImagesRequest',
        response_type_name=u'BatchAnnotateImagesResponse',
        supports_download=False,
    )

  class LocationsOperationsService(base_api.BaseApiService):
    """Service class for the locations_operations resource."""

    _NAME = u'locations_operations'

    def __init__(self, client):
      super(VisionV1.LocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (VisionLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/locations/{locationsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'vision.locations.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'VisionLocationsOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class LocationsService(base_api.BaseApiService):
    """Service class for the locations resource."""

    _NAME = u'locations'

    def __init__(self, client):
      super(VisionV1.LocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(VisionV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (VisionOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'vision.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}:cancel',
        request_field=u'cancelOperationRequest',
        request_type_name=u'VisionOperationsCancelRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (VisionOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'vision.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'VisionOperationsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (VisionOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'vision.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'VisionOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (VisionOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1/operations',
        http_method=u'GET',
        method_id=u'vision.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1/{+name}',
        request_field='',
        request_type_name=u'VisionOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )
