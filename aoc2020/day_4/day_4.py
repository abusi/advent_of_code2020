import re
from enum import Enum

from pydantic import BaseModel, Extra, Field, validator


class eclEnum(str, Enum):
    amb = "amb"
    blu = "blu"
    brn = "brn"
    gry = "gry"
    grn = "grn"
    hzl = "hzl"
    oth = "oth"


def make_passport(inp):
    r = []
    c = {}
    for line in inp:
        if len(line) > 1:
            d = line.split(" ")
            for e in d:
                f = e.split(":")
                c[f[0]] = f[1].strip()
        else:
            r.append(c)
            c = {}
    r.append(c)
    return r


_RCM = re.compile("^([0-9]{2,3})([a-z]{2})$")


class PP(BaseModel):
    byr: int = Field(...)
    iyr: int = Field(...)
    eyr: int = Field(...)
    hgt: str = Field(...)
    hcl: str = Field(...)
    ecl: eclEnum = Field(...)
    pid: str = Field(..., min_length=9, max_length=9)

    class Config:
        extra = Extra.allow

    @validator("byr")
    def val_byr(cls, v):
        if v < 1920 or v > 2002:
            raise ValueError()
        return v

    @validator("iyr")
    def val_iyr(cls, v):
        if v < 2010 or v > 2020:
            raise ValueError()
        return v

    @validator("eyr")
    def val_eyr(cls, v):
        if v < 2020 or v > 2030:
            raise ValueError()
        return v

    @validator("hgt")
    def val_hgt(cls, v: str):
        if v.endswith("cm"):
            t = int(v.strip("cm"))
            if t < 150 or t > 193:
                raise ValueError()
            return v
        if v.endswith("in"):
            t = int(v.strip("in"))
            if t < 59 or t > 76:
                raise ValueError()
            return v
        raise ValueError()

    @validator("pid")
    def val_pid(cls, v):
        try:
            return int(v)
        except Exception:
            raise ValueError()

    @validator("hcl")
    def val_hcl(cls, v):
        if not v.startswith("#"):
            raise ValueError()

        try:
            return int(v[1:], 16)
        except Exception:
            raise ValueError()


def stages(inp):
    valid_1 = 0
    valid_2 = 0
    for pp in inp:
        if (
            "byr" in pp
            and "iyr" in pp
            and "eyr" in pp
            and "hgt" in pp
            and "hcl" in pp
            and "ecl" in pp
            and "pid" in pp
        ):
            valid_1 += 1

            try:
                pp = PP(**pp)
                valid_2 += 1
            except Exception as e:
                pass

    return valid_1, valid_2


def solve(inp):
    r = make_passport(inp)

    s1, s2 = stages(r)

    print(f"One: {s1}")
    print(f"Two: {s2}")
