import logging
import subprocess

from django.http import HttpResponse
from django.views.decorators import http, csrf

logger = logging.getLogger('script_handler')
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename="script_handler.log",
                    filemode='a',
                    format='%(asctime)s %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


@http.require_POST
@csrf.csrf_exempt
def execute(request):
    command = request.POST.get("command")
    logging.info(f"Executing {command}")
    subprocess.Popen(command)
    return HttpResponse()
