import google.generativeai as genai
import os
import argparse
import subprocess
import json

# response = model.generate_content('please giveme a json test')

class Analizer:

    generation_config = {
        "temperature": 0.2,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json"
    }

    def __init__(self):
        
        genai.configure(api_key=os.environ['API_KEY'])

        with open('instructions.txt', 'r') as file:
            self.instructions = file.read()
            file.close()

        model = genai.GenerativeModel(
            model_name='gemini-pro',
            # model_name='gemini-1.5-flash',
            generation_config=self.generation_config,
            system_instruction=self.instructions
        )

        parser = argparse.ArgumentParser(
            prog='Analizer',
            description='',
            epilog='by khristopher pineda')

        parser.add_argument('-p', '--project', type=str, default=False)
        
        args = parser.parse_args()

        if not os.path.exists(args.project):
            print("The path does not exist.")

        self.project_path = args.project

        result = subprocess.run([
            'find', self.project_path, '-type', 'f', '-exec', 'sh', '-c',
            'echo "{} \n" && cat {} && echo -e "\n"', ';'
        ],  capture_output=True, text=True, errors='ignore')

        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        "/sysx/progs/api/oauthtokendao/src/controller/Token.controller.ts\n/sysx/progs/api/oauthtokendao/src/source/data.ts\ninterface data{APP_IP:string,BD_TYPE_POSTGRES:string,BD_POSTGRES_PORT:number,BD_AFORECOPPELCOM_HOST:string,BD_AFORECOPPELCOM_USERNAME:string,BD_AFORECOPPELCOM_PASSWORD:string,BD_AFORECOPPELCOM_CONNECTION_NAME:string,BD_AFORECOPPELCOM_DATABASE_NAME:string,APP_OAUTHTOKENDAO_PORT:number,APP_OAUTHTOKENDAO_NAME:string,APP_OAUTHTOKENDAO_ROUTE_GET:string,APP_OAUTHTOKENDAO_ROUTE_VALIDATE:string,APP_MICROSERVICES_CERTIFICATE:string,APP_MICROSERVICES_KEY:string,APP_MICROSERVICES_CA_BUNDLE_TRUST:string,APP_MICROSERVICES_CA_BUNDLE:string,APP_KEY_CIFRAR:string,APP_IV_CIFRAR:string,CRED_LOGINEDOCTA:string}const structure:data={...require('/sysx/progs/web/conf/config.json')};export default structure\n/sysx/progs/api/oauthtokendao/src/entity/Token.entity.ts\n/sysx/progs/api/oauthtokendao/src/routes.ts\n/sysx/progs/api/oauthtokendao/src/index.ts\n/sysx/progs/api/oauthtokendao/tsconfig.json\n/sysx/progs/api/oauthtokendao/oauthservice.drawio\n/sysx/progs/api/oauthtokendao/oauthservice.xml\n/sysx/progs/api/oauthtokendao/package.json\n/sysx/progs/api/oauthtokendao/ormconfig.json\n/sysx/progs/api/oauthtokendao/oauthservice.jpg\n/sysx/progs/api/oauthtokendao/Dockerfile\n/sysx/progs/api/oauthtokendao/package-lock.json\n/sysx/progs/api/oauthtokendao/README.md",
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "{\"description\": \"This project appears to be a TypeScript node application, containing a simple REST API.\", \"language\": \"TypeScript\", \"configurations\": [{\"key\": \"APP_IP\", \"value\": \"\"}, {\"key\": \"BD_TYPE_POSTGRES\", \"value\": \"\"}, {\"key\": \"BD_POSTGRES_PORT\", \"value\": \"\"}, {\"key\": \"BD_AFORECOPPELCOM_HOST\", \"value\": \"\"}, {\"key\": \"BD_AFORECOPPELCOM_USERNAME\", \"value\": \"\"}, {\"key\": \"BD_AFORECOPPELCOM_PASSWORD\", \"value\": \"\"}, {\"key\": \"BD_AFORECOPPELCOM_CONNECTION_NAME\", \"value\": \"\"}, {\"key\": \"BD_AFORECOPPELCOM_DATABASE_NAME\", \"value\": \"\"}, {\"key\": \"APP_OAUTHTOKENDAO_PORT\", \"value\": \"\"}, {\"key\": \"APP_OAUTHTOKENDAO_NAME\", \"value\": \"\"}, {\"key\": \"APP_OAUTHTOKENDAO_ROUTE_GET\", \"value\": \"\"}, {\"key\": \"APP_OAUTHTOKENDAO_ROUTE_VALIDATE\", \"value\": \"\"}, {\"key\": \"APP_MICROSERVICES_CERTIFICATE\", \"value\": \"\"}, {\"key\": \"APP_MICROSERVICES_KEY\", \"value\": \"\"}, {\"key\": \"APP_MICROSERVICES_CA_BUNDLE_TRUST\", \"value\": \"\"}, {\"key\": \"APP_MICROSERVICES_CA_BUNDLE\", \"value\": \"\"}, {\"key\": \"APP_KEY_CIFRAR\", \"value\": \"\"}, {\"key\": \"APP_IV_CIFRAR\", \"value\": \"\"}, {\"key\": \"CRED_LOGINEDOCTA\", \"value\": \"\"}]}\n",
                    ],
                },
            ]
        )
        
        response = chat_session.send_message(result.stdout)

        print(response.text)

if __name__ == '__main__':
    app = Analizer()