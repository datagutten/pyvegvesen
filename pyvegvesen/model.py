from __future__ import annotations
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Extra

class KjoretoyBaseModel(BaseModel):
        class Config:
            extra = Extra.allow

class KjoretoyId(KjoretoyBaseModel):
    kjennemerke: Optional[str] = None
    understellsnummer: Optional[str] = None


class Forstegangsregistrering(KjoretoyBaseModel):
    registrertForstegangNorgeDato: Optional[str] = None


class Kjennemerketype(KjoretoyBaseModel):
    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class KjennemerkeItem(KjoretoyBaseModel):

    fomTidspunkt: Optional[str] = None
    kjennemerke: Optional[str] = None
    kjennemerkekategori: Optional[str] = None
    kjennemerketype: Optional[Kjennemerketype] = None


class KjoringensArt(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class Registreringsstatus(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class Registrering(KjoretoyBaseModel):

    fomTidspunkt: Optional[str] = None
    kjoringensArt: Optional[KjoringensArt] = None
    registreringsstatus: Optional[Registreringsstatus] = None
    registrertForstegangPaEierskap: Optional[str] = None


class Godkjenningsundertype(KjoretoyBaseModel):

    kodeNavn: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class KvalitetskodeForstegangRegDato(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class ForstegangsGodkjenning(KjoretoyBaseModel):

    forstegangRegistrertDato: Optional[str] = None
    godkjenningsId: Optional[str] = None
    godkjenningsundertype: Optional[Godkjenningsundertype] = None
    gyldigFraDato: Optional[str] = None
    gyldigFraDatoTid: Optional[str] = None
    kvalitetskodeForstegangRegDato: Optional[KvalitetskodeForstegangRegDato] = None
    unntak: Optional[List] = None


class KjoretoymerknadItem(KjoretoyBaseModel):

    merknad: Optional[str] = None
    merknadtypeKode: Optional[str] = None


class Registreringsbegrensninger(KjoretoyBaseModel):

    registreringsbegrensning: Optional[List] = None


class Typegodkjenningnummer(KjoretoyBaseModel):

    direktiv: Optional[str] = None
    land: Optional[str] = None
    serie: Optional[str] = None
    utvidelse: Optional[str] = None


class EfTypegodkjenning(KjoretoyBaseModel):

    typegodkjenningNrTekst: Optional[str] = None
    typegodkjenningnummer: Optional[Typegodkjenningnummer] = None
    variant: Optional[str] = None


class KjoretoyAvgiftsKode(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class NasjonalGodkjenning(KjoretoyBaseModel):

    nasjonaltGodkjenningsAr: Optional[str] = None
    nasjonaltGodkjenningsHovednummer: Optional[str] = None
    nasjonaltGodkjenningsUndernummer: Optional[str] = None


class TekniskKode(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class TekniskUnderkode(KjoretoyBaseModel):

    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class Kjoretoyklassifisering(KjoretoyBaseModel):

    beskrivelse: Optional[str] = None
    efTypegodkjenning: Optional[EfTypegodkjenning] = None
    kjoretoyAvgiftsKode: Optional[KjoretoyAvgiftsKode] = None
    nasjonalGodkjenning: Optional[NasjonalGodkjenning] = None
    spesielleKjennetegn: Optional[str] = None
    tekniskKode: Optional[TekniskKode] = None
    tekniskUnderkode: Optional[TekniskUnderkode] = None
    iSamsvarMedTypegodkjenning: Optional[bool] = None


class Kravomrade(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class Kravoppfyllelse(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class KravItem(KjoretoyBaseModel):

    kravomrade: Optional[Kravomrade] = None
    kravoppfyllelse: Optional[Kravoppfyllelse] = None


class AkselItem(KjoretoyBaseModel):

    egenvektAksel: Optional[int] = None
    id: Optional[int] = None
    plasseringAksel: Optional[str] = None
    tekniskTillattAkselLast: Optional[int] = None


class AkselListe(KjoretoyBaseModel):

    aksel: Optional[List[AkselItem]] = None


class AkselGruppeItem(KjoretoyBaseModel):

    akselListe: Optional[AkselListe] = None
    egenvektAkselGruppe: Optional[int] = None
    id: Optional[int] = None
    plasseringAkselGruppe: Optional[str] = None
    tekniskTillattAkselGruppeLast: Optional[int] = None


class Akslinger(KjoretoyBaseModel):

    akselGruppe: Optional[List[AkselGruppeItem]] = None
    antallAksler: Optional[int] = None


class Bremser(KjoretoyBaseModel):

    tilhengerBremseforbindelse: Optional[List] = None


class AkselDekkOgFelgItem(KjoretoyBaseModel):

    akselId: Optional[int] = None
    belastningskodeDekk: Optional[str] = None
    dekkdimensjon: Optional[str] = None
    felgdimensjon: Optional[str] = None


class AkselDekkOgFelgKombinasjonItem(KjoretoyBaseModel):

    akselDekkOgFelg: Optional[List[AkselDekkOgFelgItem]] = None


class DekkOgFelg(KjoretoyBaseModel):

    akselDekkOgFelgKombinasjon: Optional[List[AkselDekkOgFelgKombinasjonItem]] = None


class Dimensjoner(KjoretoyBaseModel):

    bredde: Optional[int] = None
    lengde: Optional[int] = None


class MerkeItem(KjoretoyBaseModel):

    merke: Optional[str] = None
    merkeKode: Optional[str] = None


class Generelt(KjoretoyBaseModel):

    fabrikant: Optional[List] = None
    handelsbetegnelse: Optional[List[str]] = None
    merke: Optional[List[MerkeItem]] = None
    tekniskKode: Optional[TekniskKode] = None
    typebetegnelse: Optional[str] = None


class KjennemerketypeBak(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeTypeId: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class KjennemerkestorrelseBak(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeTypeId: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class KjennemerketypeForan(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeTypeId: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class KjennemerkestorrelseForan(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeTypeId: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class PlasseringFabrikasjonsplateItem(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeTypeId: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class PlasseringUnderstellsnummerItem(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeTypeId: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class KarosseriOgLasteplan(KjoretoyBaseModel):

    antallDorer: Optional[List] = None
    dorUtforming: Optional[List] = None
    kjennemerketypeBak: Optional[KjennemerketypeBak] = None
    kjennemerkestorrelseBak: Optional[KjennemerkestorrelseBak] = None
    kjennemerketypeForan: Optional[KjennemerketypeForan] = None
    kjennemerkestorrelseForan: Optional[KjennemerkestorrelseForan] = None
    kjoringSide: Optional[str] = None
    plasseringFabrikasjonsplate: Optional[List[PlasseringFabrikasjonsplateItem]] = None
    plasseringUnderstellsnummer: Optional[List[PlasseringUnderstellsnummerItem]] = None
    rFarge: Optional[List] = None


class DrivstoffKodeMiljodata(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeTypeId: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class MiljoOgdrivstoffGruppeItem(KjoretoyBaseModel):

    drivstoffKodeMiljodata: Optional[DrivstoffKodeMiljodata] = None
    lyd: Optional[Dict[str, Any]] = None


class Miljodata(KjoretoyBaseModel):

    miljoOgdrivstoffGruppe: Optional[List[MiljoOgdrivstoffGruppeItem]] = None


class HybridKategori(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeTypeId: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class DrivstoffKode(KjoretoyBaseModel):

    kodeBeskrivelse: Optional[str] = None
    kodeNavn: Optional[str] = None
    kodeTypeId: Optional[str] = None
    kodeVerdi: Optional[str] = None
    tidligereKodeVerdi: Optional[List] = None


class DrivstoffItem(KjoretoyBaseModel):

    drivstoffKode: Optional[DrivstoffKode] = None
    maksNettoEffekt: Optional[float] = None


class MotorItem(KjoretoyBaseModel):

    drivstoff: Optional[List[DrivstoffItem]] = None
    slagvolum: Optional[int] = None


class MotorOgDrivverk(KjoretoyBaseModel):

    girutvekslingPrGir: Optional[List] = None
    hybridKategori: Optional[HybridKategori] = None
    maksimumHastighet: Optional[List] = None
    maksimumHastighetMalt: Optional[List] = None
    motor: Optional[List[MotorItem]] = None


class OvrigeTekniskeDatum(KjoretoyBaseModel):

    datafeltNavn: Optional[str] = None
    datafeltVerdi: Optional[str] = None


class Persontall(KjoretoyBaseModel):

    sitteplasserForan: Optional[int] = None
    sitteplasserTotalt: Optional[int] = None


class Tilhengerkopling(KjoretoyBaseModel):

    kopling: Optional[List] = None


class Vekter(KjoretoyBaseModel):

    egenvekt: Optional[int] = None
    egenvektMinimum: Optional[int] = None
    nyttelast: Optional[int] = None
    tillattTilhengervektMedBrems: Optional[int] = None
    tillattTilhengervektUtenBrems: Optional[int] = None
    tillattTotalvekt: Optional[int] = None
    vogntogvektAvhBremsesystem: Optional[List] = None


class TekniskeData(KjoretoyBaseModel):

    akslinger: Optional[Akslinger] = None
    bremser: Optional[Bremser] = None
    dekkOgFelg: Optional[DekkOgFelg] = None
    dimensjoner: Optional[Dimensjoner] = None
    generelt: Optional[Generelt] = None
    karosseriOgLasteplan: Optional[KarosseriOgLasteplan] = None
    miljodata: Optional[Miljodata] = None
    motorOgDrivverk: Optional[MotorOgDrivverk] = None
    ovrigeTekniskeData: Optional[List[OvrigeTekniskeDatum]] = None
    persontall: Optional[Persontall] = None
    tilhengerkopling: Optional[Tilhengerkopling] = None
    vekter: Optional[Vekter] = None


class TekniskGodkjenning(KjoretoyBaseModel):

    godkjenningsId: Optional[str] = None
    godkjenningsundertype: Optional[Godkjenningsundertype] = None
    gyldigFraDato: Optional[str] = None
    gyldigFraDatoTid: Optional[str] = None
    kjoretoyklassifisering: Optional[Kjoretoyklassifisering] = None
    krav: Optional[List[KravItem]] = None
    tekniskeData: Optional[TekniskeData] = None
    unntak: Optional[List] = None


class Godkjenning(KjoretoyBaseModel):

    forstegangsGodkjenning: Optional[ForstegangsGodkjenning] = None
    kjoretoymerknad: Optional[List[KjoretoymerknadItem]] = None
    registreringsbegrensninger: Optional[Registreringsbegrensninger] = None
    tekniskGodkjenning: Optional[TekniskGodkjenning] = None
    tilleggsgodkjenninger: Optional[List] = None


class PeriodiskKjoretoyKontroll(KjoretoyBaseModel):

    sistGodkjent: Optional[str] = None
    kontrollfrist: Optional[str] = None


class KjoretoydataListeItem(KjoretoyBaseModel):

    kjoretoyId: Optional[KjoretoyId] = None
    forstegangsregistrering: Optional[Forstegangsregistrering] = None
    kjennemerke: Optional[List[KjennemerkeItem]] = None
    registrering: Optional[Registrering] = None
    godkjenning: Optional[Godkjenning] = None
    periodiskKjoretoyKontroll: Optional[PeriodiskKjoretoyKontroll] = None


class Model(KjoretoyBaseModel):

    kjoretoydataListe: Optional[List[KjoretoydataListeItem]] = None