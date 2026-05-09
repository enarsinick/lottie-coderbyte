# format_time

Given a non-negative integer number of seconds, return a string in the form
`"HH:MM:SS"` — hours, minutes, and seconds, each zero-padded to two digits.

You can assume the input is less than 24 hours (i.e. less than 86400).

## Examples
| Call | Result |
| --- | --- |
| `format_time(0)` | `"00:00:00"` |
| `format_time(59)` | `"00:00:59"` |
| `format_time(60)` | `"00:01:00"` |
| `format_time(3600)` | `"01:00:00"` |
| `format_time(3661)` | `"01:01:01"` |
| `format_time(86399)` | `"23:59:59"` |

## Concepts exercised
- integer division `//` and modulo `%`
- f-strings with zero-padding (`f"{x:02d}"`)
- breaking a number into named pieces (hours, minutes, seconds)

## Hints

<details><summary>Hint 1 — getting started</summary>

There are 60 seconds in a minute and 60 minutes in an hour. So you need to
turn the total number of seconds into three pieces: hours, leftover minutes,
and leftover seconds.
</details>

<details><summary>Hint 2 — division and modulo</summary>

- `total // 3600` gives whole hours
- `(total % 3600) // 60` gives the leftover minutes
- `total % 60` gives the leftover seconds

Then you need to format each as two digits. An f-string with `:02d` does that:
`f"{hours:02d}"` formats `5` as `"05"` and `12` as `"12"`.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
hours   = secs divided by 3600 (integer division)
minutes = (secs modulo 3600) divided by 60 (integer division)
seconds = secs modulo 60
return the f-string "{hours:02d}:{minutes:02d}:{seconds:02d}"
```

The `:02d` part means "format as a decimal integer, at least 2 digits, padded
on the left with zeros".
</details>
