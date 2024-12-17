## Archiving format with built-in error detection and recovery

2024-12-14

Once upon a time I went down a rabbit hole when looking for a data backup solution. I learned about things like deduplication, incremental backups, checksums, the 3-2-1 strategy, error recovery, par2, reed-solomon encoding, zfs, etc.

It seems there are few options for compression or archiving tools with wide support for error integrity and detection:

- rar (`-rr` option, which uses Reed-Solomon coding)
- lzip (recovers single bit flips only)
- use whatever compression and encryption you want, then par2 the files, and store both the original archives and the par2 files.

\#idea: Create an open source rar alternative with error detection and recovery. Maybe add Reed-Solomon coding to 7z archives. Or just par2 a 7z file and tar the 7z file and the par2 files.


### Topics

- Compression
- Error detection and recovery
- Seekability


### Links

[desiderata](https://news.ycombinator.com/item?id=32222183)

[Safety of the lzip format](https://www.nongnu.org/lzip/safety_of_the_lzip_format.html)

