from pygame import image, transform, Surface, BLEND_MULT

def create_sprite_from_str(sprite: str, color: str, width: int, height: int):
    loaded_sprite = image.load(sprite).convert_alpha()
    loaded_sprite = transform.scale(loaded_sprite, (width, height))

    colored_image = Surface(loaded_sprite.get_size()).convert_alpha()
    colored_image.fill(color)
    final_sprite = loaded_sprite.copy()
    final_sprite.blit(colored_image, (0, 0), special_flags = BLEND_MULT)

    return final_sprite

def create_sprite_from_str_dual(sprite: str, color1: str, color2: str, width: int, height: int):
    loaded_sprite = image.load(sprite).convert_alpha()
    loaded_sprite = transform.scale(loaded_sprite, (width, height))

    colored_image1 = Surface(loaded_sprite.get_size()).convert_alpha()
    colored_image2 = Surface(loaded_sprite.get_size()).convert_alpha()
    colored_image1.fill(color1)
    colored_image2.fill(color2)

    final_sprite = loaded_sprite.copy()
    final_sprite.blit(colored_image1, (0, 0), special_flags = BLEND_MULT)
    final_sprite.blit(colored_image2, (0, height / 2), special_flags = BLEND_MULT)

    return final_sprite

def create_sprite_from_surface(sprite: Surface, color: str, width: int | None = None, height: int | None = None):
    if width and height:
        sprite = transform.scale(sprite, (width, height))
    colored_image = Surface(sprite.get_size()).convert_alpha()
    colored_image.fill(color)
    final_sprite = sprite.copy()
    final_sprite.blit(colored_image, (0, 0), special_flags = BLEND_MULT)
    return final_sprite
