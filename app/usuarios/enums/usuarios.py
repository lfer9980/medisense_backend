from core.base import StrEnum


class UserType(StrEnum):
    Admin = 'admin'
    Paciente = 'paciente'
    PersonalSalud = 'personal_salud'
    Asistente = 'asistente'
