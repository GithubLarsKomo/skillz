---
name: sport-training-music
description: Erstellt präferenzbasierte Musikprofile und Session-Empfehlungen für Aktivierung, Motivation, Affekt, Warm-up, Training und Recovery. Verwenden für Trainingsmusik nach Athletenpräferenzen; BPM und Genre nicht als starre Leistungs- oder Intensitätsformel behandeln.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-athlete-profile
  - sport-microcycle-planning
outputs:
  - training-music-profile.json
lastEvaluated: 2026-08-22
---

# Sport Training Music

Nutze Musik als individualisierbaren Kontextreiz für Motivation, Affekt, Aktivierung und subjektive Trainingsqualität. Präferenz und Nutzbarkeit haben Vorrang vor vermeintlich optimalen Genres oder BPM-Zahlen.

## Trigger

Nutze diesen Skill für Warm-up-/Training-/Recovery-Playlists, Motivationsunterstützung, gewünschte Aktivierung vor Schlüsselreizen oder wenn Musik gezielt an Sessiontypen angepasst werden soll.

## Voraussetzungen

Bevorzugte Künstler/Genres/Tracks, explizite Ausschlüsse, Nutzungssituation und gewünschter Effekt sind wichtiger als demografische Annahmen. Hörsicherheit, Umgebung und Wettkampfregeln berücksichtigen.

## Ablauf

1. **Präferenzen erfassen.** Lieblings-/No-go-Musik, Vertrautheit, Lyrics-/Instrumental-Präferenz und explizite Ausschlüsse speichern.
2. **Sessionziel bestimmen.** Aktivierung, Motivation, Affekt, Rhythmusgefühl, Ablenkung oder Down-regulation als Zweck definieren.
3. **Timing wählen.** Pre-task/Warm-up, während der Einheit, Pausen oder Recovery unterscheiden.
4. **Tracks nach Präferenz priorisieren.** Self-selected/preferred music bevorzugen, wenn sie zum Zweck passt; kein Genre allein als ergogen deklarieren.
5. **Tempo nur als Hinweis verwenden.** BPM kann Aktivierungscharakter beschreiben, ist aber kein valider Ersatz für Trainingszone, Herzfrequenz, Power oder RPE.
6. **Kontext prüfen.** Technik-/Sicherheitsanforderungen, Verkehr, Wasser, Kommunikation mit Trainer/Team und Wettkampfregeln können Musik einschränken.
7. **Response lernen.** Gefallen, Motivation, wahrgenommene Anstrengung, Fokus und Session-Adhärenz beobachten; Playlist entsprechend individualisieren.

## Evidenzgrenze

Bevorzugte Musik kann Motivation, Affekt und manche Leistungsparameter verbessern, die Befunde sind je nach Aufgabe und Outcome heterogen. Keine Garantie auf Leistungssteigerung und keine Ableitung „höhere Intensität = exakt höherer BPM“.

## Safety

Musik darf Umgebungswahrnehmung, Verkehrssicherheit, Wasser-/Bootskommunikation, technische Cues oder medizinische Warnsignale nicht überdecken. Lautstärke/Hördauer nicht als Leistungsvariable maximieren.

## Alters-/Geschlechtsmodifier

Keine alters- oder geschlechtsbasierten Genreannahmen. Explizite Präferenz dominiert demografische Stereotype.

## Prüfungen

- Sind Zweck und Timing der Musik klar?
- Werden Präferenzen und Ausschlüsse respektiert?
- Ist BPM nur Kontext und nicht Trainingsregler?
- Sind Sicherheits-/Kommunikationssituationen berücksichtigt?
- Kann die Empfehlung aus individueller Response lernen?

## Fehlerbehandlung

- **Keine Präferenzen bekannt:** kleine Auswahl/Probe statt angeblich optimaler Playlist.
- **Musik stört Technik/Fokus:** reduzieren, Timing verschieben oder weglassen.
- **Sicherheitskritische Umgebung:** keine Empfehlung zum Musikhören während der Exposition.

## Übergabe

`training-music-profile.json` enthält Version, Präferenzen, Ausschlüsse, Session-Ziele, Aktivierungswunsch, Timing, Auswahlregeln, optionale BPM-Bandbreiten als deskriptiven Kontext, Safety Constraints und Feedbackfelder.

## Abschlusskriterien

Die Empfehlung ist personalisiert, zweckgebunden, sicherheitsgeprüft und vermeidet starre BPM-/Genre-Rezepte.
