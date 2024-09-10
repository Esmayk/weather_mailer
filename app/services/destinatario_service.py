from .usuario_service import UsuarioService

class DestinatarioService:
    def __init__(self) -> None:
        pass

    def get_emails(): 
        try:
            recipient = []
            usuarios = UsuarioService.buscar_usuarios()
            recipient = [usuario.get('email') for usuario in usuarios]
            recipient = ','.join(recipient)
        except Exception as e:
            print(f"Erro ao buscar destinatario: {e}")
        return  recipient