from django.conf import settings

import requests
from rest_framework.views import APIView
from rest_framework.response import Response


class ProxyPoladsView(APIView):
    base_api_url = settings.POLADS_BASE_API_URL

    def _request(self, path, query_parameters):
        return requests.get(
            f"{self.base_api_url}{path}",
            params=query_parameters,
            headers={
                'Authorization': settings.POLADS_API_TOKEN
            }
        )

    def get(self, request, *args, **kwargs):
        # Get Polads API path from current path
        polads_path = request.path[7:]

        try:
            # Request to Polads API
            req_polads = self._request(
                polads_path,
                request.GET
            )
            req_polads.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return Response(
                e.response.text,
                status=e.response.status_code
            )

        # Handle 204 no content error on json decode
        if req_polads.status_code == 204:
            return Response(
                req_polads.text,
                status=req_polads.status_code
            )

        return Response(
            req_polads.json(),
            status=req_polads.status_code
        )
