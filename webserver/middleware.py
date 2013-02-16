
class XUACompatibleMiddleware(object):
	def process_response(self, request, response):
		response['X-UA-Compatible'] = 'IE=edge,chrome=1'
		return response
