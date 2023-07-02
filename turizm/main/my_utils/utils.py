import django.db.models


def table_model(model: django.db.models.Model) -> str:
    model_query = model.objects.all()
    model_list = []
    for user in model_query:
        model_list.append(user.to_string())

    model_str = '<br>'.join(model_list)

    return model_str
