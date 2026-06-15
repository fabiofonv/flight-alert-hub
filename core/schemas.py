from pydantic import BaseModel, Field
from typing import Optional

class VooOportunidade(BaseModel):
    trecho: str = Field(..., description="Exemplo: CPV-BSB")
    data: str = Field(..., description="Formato: DD/MM/AAAA")
    horario: str = Field(..., description="Horário de partida, Exemplo: 15:00")
    tempo_viagem: str = Field(..., description="Duração total do voo")
    stopover: bool = Field(default=False, description="Indica se há uma conexão longa/intencional")
    reais: Optional[float] = Field(None, description="Preço da passagem em dinheiro")
    pontos: Optional[int] = Field(None, description="Preço da passagem em milhas")

    # Validação customizada extra (opcional) para garantir integridade econômica
    def verificar_precos(self) -> bool:
        return self.reais is not None or self.pontos is not None