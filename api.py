import requests
import subprocess
import simplejson as json

from mic import record


KEY = "RMIPQ0GLPUFY3NVEH"
BASE_URL = "http://developer.echonest.com/api/v4/song/{0}"
file_name = "sample.wav"

def identify(params):

    params["api_key"] = KEY
    params["version"] = "4.12"

    url = BASE_URL.format("identify")

    response = requests.get(url, params=params)
    return response.json()

def generate_code():

    record(seconds=30, file_name=file_name)

    process = subprocess.Popen(["echoprint-codegen", file_name, "0", "60"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()

    data = json.loads(out)
    return data[0]["code"]


code = generate_code()

params = {
    "code": code
}

print identify(params)