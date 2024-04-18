from django.contrib import admin

from palette.models import Palette, Color, ColorInPalette


class ColorInline(admin.TabularInline):
    model = ColorInPalette
    extra = 2
    min_num = 1


@admin.register(Palette)
class PaletteAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "get_colors")
    list_filter = ("name",)
    empty_value_display = "--пусто--"
    inlines = (ColorInline,)

    @admin.display(description="Цвета")
    def get_colors(self, obj):
        return '\n '.join([
            f'{item["color__name"]}'
            for item in obj.color_list.values(
                'color__name'
            )
        ])


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "hex")
    empty_value_display = "--пусто--"
