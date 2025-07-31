import django_tables2 as tables
from django_tables2.utils import A
from django.urls import reverse
from django.utils.html import format_html
from . models import Ville

class VilleTable(tables.Table):
    nom = tables.Column(
        verbose_name="Nom",
        attrs={"th": {"class": "nom-header"}}
    )

    code_postal = tables.Column(
        verbose_name="Code postal",
        attrs={"th": {"class": "code-postal-header"}}
    )

    created_at = tables.DateColumn(
        verbose_name = "Créé le ",
        format="j F Y",
        attrs={"th": {"class": "date-header"}}
    )

    utilisateur = tables.Column(
        verbose_name = "Utilisateur",
        attrs={"th": {"class": "utilisateur-header"}}
    )

    actions = tables.TemplateColumn(
        template_name='partials/ville_actions.html',
        verbose_name="Édition",
        orderable=False,
        attrs={"th": {"class": "actions-header"}}
    )

    class Meta:
        model = Ville
        template_name = "django_tables2/bootstrap4.html"
        fields = ("nom", "code_postal", "created_at", "utilisateur", "actions")
        attrs = {
            "class": "custom-table",
            "id": "villes-table"
        }

        empty_text = "Aucune ville trouvée."

        def render_nom(self, value, record):
            return format_html('<strong>{}</strong>', value)

        def render_code_postal(self,value):
            return format_html('<code>{}</code>', value)
        
        
