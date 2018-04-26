from __future__ import absolute_import
from . import BaseProxy
from ..requests import Request, POST


class PackageProxy(BaseProxy):

    def get(self, ownername, projectname, packagename):
        """
        Return a package
        :param str ownername:
        :param str projectname:
        :param str packagename:
        :return: Munch
        """
        endpoint = "/package"
        params = {
            "ownername": ownername,
            "projectname": projectname,
            "packagename": packagename,
        }
        request = Request(endpoint, api_base_url=self.api_base_url, params=params)
        response = request.send()
        return response.munchify()

    def get_list(self, ownername, projectname, pagination=None):
        """
        Return a list of packages
        :param str ownername:
        :param str projectname:
        :param pagination:
        :return: Munch
        """
        endpoint = "/package/list"
        params = {
            "ownername": ownername,
            "projectname": projectname,
        }
        params.update(pagination.to_dict() if pagination else {})

        request = Request(endpoint, api_base_url=self.api_base_url, params=params)
        response = request.send()
        return response.munchify()

    def add(self, ownername, projectname, packagename, source_type_text, source_dict):
        """
        Add a package to a project
        :param str ownername:
        :param str projectname:
        :param str packagename:
        :param str source_type_text:
        :param source_dict:
        :return: Munch
        """
        endpoint = "/package/add"
        data = {
            "ownername": ownername,
            "projectname": projectname,
            "package_name": packagename,
            "source_type_text": source_type_text,
        }
        data.update(source_dict)
        request = Request(endpoint, api_base_url=self.api_base_url, data=data, method=POST, auth=self.auth)
        response = request.send()
        return response.munchify()

    def edit(self, ownername, projectname, packagename, source_type_text, source_dict):
        """
        Edit a package in a project
        :param str ownername:
        :param str projectname:
        :param str packagename:
        :param source_type_text:
        :param source_dict:
        :return: Munch
        """
        endpoint = "/package/edit"
        data = {
            "ownername": ownername,
            "projectname": projectname,
            "package_name": packagename,
            "source_type_text": source_type_text,
        }
        data.update(source_dict)
        request = Request(endpoint, api_base_url=self.api_base_url, data=data, method=POST, auth=self.auth)
        response = request.send()
        return response.munchify()

    def reset(self, ownername, projectname, packagename):
        """
        Reset a package configuration
        :param str ownername:
        :param str projectname:
        :param str packagename:
        :return: Munch
        """
        endpoint = "/package/reset"
        data = {
            "ownername": ownername,
            "projectname": projectname,
            "package_name": packagename,
        }
        request = Request(endpoint, api_base_url=self.api_base_url, data=data, method=POST, auth=self.auth)
        response = request.send()
        return response.munchify()

    def build(self, ownername, projectname, packagename, buildopts=None):
        """
        Create a build from a package configuration
        :param str ownername:
        :param str projectname:
        :param str packagename:
        :param buildopts:
        :return: Munch
        """
        endpoint = "/package/build"
        data = {
            "ownername": ownername,
            "projectname": projectname,
            "package_name": packagename,
        }
        data.update(buildopts or {})
        request = Request(endpoint, api_base_url=self.api_base_url, data=data, method=POST, auth=self.auth)
        response = request.send()
        return response.munchify()

    def delete(self, ownername, projectname, packagename):
        """
        Delete a package from a project
        :param str ownername:
        :param str projectname:
        :param str packagename:
        :return: Munch
        """
        endpoint = "/package/delete"
        data = {
            "ownername": ownername,
            "projectname": projectname,
            "package_name": packagename,
        }
        request = Request(endpoint, api_base_url=self.api_base_url, data=data, method=POST, auth=self.auth)
        response = request.send()
        return response.munchify()