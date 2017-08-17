from django import template
register = template.Library()


@register.inclusion_tag("tags/person.html", name="person")
def person(entry):
    return {"person": entry}


@register.inclusion_tag("tags/form.html", name="form_body")
def form_body(entry):
    return {"form": entry}
