# odoo-time-report — gren 19.0

> **Denna gren är avsiktligt tom.** Modulerna är INTE portade till Odoo 19.
> Grenen finns så att dev-miljöer (`hansolo19`) kan klona den utan att falla,
> men den påstår ingenting om att koden är portad.

## Baseline

| | |
|---|---|
| Källa | `20.0` |
| Moduler | **1** |
| Grenar i repot | `14.0`, `16.0`, `18.0`, `20.0`, `main` |

## Moduler

- `time_report_automation`

## Blockerare

**1 externa beroenden saknas** i Odoo 19-kärnan och OCA 19.0:

| Beroende | Behövs av |
|---|---|
| `hr_timesheet_sheet` | `time_report_automation` |

### Prioritering

Ett beroende som blockerar många moduler ger mest nytta att lösa först:

- `hr_timesheet_sheet` — frisläpper **1** modul(er)

## Nästa steg

Portering sker på `*-pfile`-maskin med versionsagnostisk kod
(`.p.py` / `.p.xml`). Se `/skill:odoo-pfiles`.
