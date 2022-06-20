# Vaccinations-API

This is a **API** for register the vaccine table for SAR-COV19 or other vaccines.

Here you can cadastre patients in a database for know the vaccine, first shot and when he comeback, knowing the names, the health unit and the vaccine name.

You can consult this API with a end point GET:"/vaccinations" to receive a list, for consulting the register is a end point with POST:"/vaccinations"

## GET:/vaccinations
- No requisition body

- Response:
          
          [
          
              {
                "cpf": "5555555555",
                "name": "Takumi Inui",
                "first_shot_date": "Dia e Hora",
                "second_shot_date": "Dia e Hora 90 dias",
                "vaccine_name": "Orphanoc Vaccine",
                "health_unit_name": "Smart Brain"
              },
              {
                "cpf": "12312312312"
                "name": "Ni-Go",
                "first_shot_date": "Dia e Hora",
                "second_shot_date": "Dia e Hora 90 dias",
                "vaccine_name": "Coronavac",
                "health_unit_name": "Santa Rita"
              },
              {
                "cpf": "66666666666",
                "name": "Wataru Kurenai",
                ""first_shot_date": "Dia e Hora",
                "second_shot_date": "Dia e Hora 90 dias",
                "vaccine_name": "Fangires Vaccine",
                "health_unit_name": "Dragon Castle"
              }
              
           ]
    
## POST:/vaccinations

- Requisition :

        {
            "cpf": "12345678901",
            "name": "Tijubina",
            "vaccine_name": "Pfizer",
            "health_unit_name": "Carreta Furacao"
        }
        
- Response :

        {
          "cpf": "12345678901",
          "name": "Tijubina",
          "first_shot_date": "*Dia Datado*",
          "second_shot_date": "*Segunda dose daqui a 90 dias*",
          "vaccine_name": "Pfizer",
          "health_unit_name": "Carreta Furacao"
        }


