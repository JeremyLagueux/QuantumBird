from pygame import image, transform, Surface, BLEND_MULT

def create_sprite_from_str(sprite: str, color: str, width: int, height: int):
    loaded_sprite = image.load(sprite).convert_alpha()
    loaded_sprite = transform.scale(loaded_sprite, (width, height))

    colored_image = Surface(loaded_sprite.get_size()).convert_alpha()
    colored_image.fill(color)
    final_sprite = loaded_sprite.copy()
    final_sprite.blit(colored_image, (0, 0), special_flags = BLEND_MULT)

    return final_sprite

def create_sprite_from_surface(sprite: Surface, color: str):
    colored_image = Surface(sprite.get_size()).convert_alpha()
    colored_image.fill(color)
    final_sprite = sprite.copy()
    final_sprite.blit(colored_image, (0, 0), special_flags = BLEND_MULT)

    return final_sprite
