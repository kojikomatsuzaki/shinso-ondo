# Design Decisions

## ASCII filenames

Public filenames use ASCII only.

Reason:
Some mail clients automatically detect URLs and truncate them before Japanese filenames, resulting in broken download links.

Therefore, all publicly distributed filenames are written using ASCII characters.
