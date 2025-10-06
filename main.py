from google.cloud import service_usage_v1
from google.api_core import exceptions

import os
from dotenv import load_dotenv

def enable_gcp_services(project_id: str, services: list[str]):
    """
    Ativa uma lista de APIs em um projeto específico do GCP.

    Args:
        project_id: O ID do seu projeto no GCP.
        services: Uma lista de nomes de serviço a serem ativados
                  (ex: ['run.googleapis.com', 'bigquery.googleapis.com']).
    """
    client = service_usage_v1.ServiceUsageClient()

    for service in services:
        print(f"Verificando o serviço: {service}...")
        service_name = f"projects/{project_id}/services/{service}"

        try:
            # Tenta obter o serviço para ver se ele já está ativo
            request = service_usage_v1.GetServiceRequest(name=service_name)
            service_details = client.get_service(request=request)

            if service_details.state == service_usage_v1.State.ENABLED:
                print(f"O serviço {service} já está ATIVADO.")
                continue
            
            # Se não estiver ativo, ativa
            print(f"Ativando o serviço: {service}...")
            enable_request = service_usage_v1.EnableServiceRequest(name=service_name)
            operation = client.enable_service(request=enable_request)
            
            # Espera a operação ser concluída
            operation.result()
            print(f"Serviço {service} ativado com sucesso!")

        except exceptions.NotFound:
            print(f"ERRO: O serviço {service} não foi encontrado para o projeto {project_id}.")
        except Exception as e:
            print(f"ERRO ao tentar ativar o serviço {service}: {e}")

if __name__ == "__main__":

    load_dotenv() 

    # Substitua pelo ID do seu projeto
    gcp_project_id = os.getenv("PROJECT_ID") 

    services_to_enable = [
        "run.googleapis.com",
        "bigquery.googleapis.com",
        "pubsub.googleapis.com",
        "cloudscheduler.googleapis.com",
        "cloudbuild.googleapis.com",
        "iam.googleapis.com",
    ]

    enable_gcp_services(gcp_project_id, services_to_enable)