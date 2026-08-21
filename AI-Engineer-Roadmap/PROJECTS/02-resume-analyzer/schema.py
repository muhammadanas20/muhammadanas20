"""Target schema for resume extraction."""
from pydantic import BaseModel, Field


class Education(BaseModel):
    school: str
    degree: str | None = None
    year: int | None = None


class Resume(BaseModel):
    name: str
    skills: list[str] = Field(default_factory=list)
    years_experience: int | None = Field(default=None, ge=0, le=60)
    education: list[Education] = Field(default_factory=list)
    summary: str = Field(max_length=400)
