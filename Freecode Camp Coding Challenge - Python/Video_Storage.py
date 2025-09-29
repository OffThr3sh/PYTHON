#                                                                     Video Storage

# Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:

#     The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"), or gigabytes ("GB").
#     If not given one of the video units above, return "Invalid video unit".
#     The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
#     If not given one of the hard drive units above, return "Invalid drive unit".
#     Return the number of whole videos the drive can fit.
#     Use the following conversions:

# Unit 	Equivalent
# 1 B 	1 B
# 1 KB 	1000 B
# 1 MB 	1000 KB
# 1 GB 	1000 MB
# 1 TB 	1000 GB

# For example, given 500, "MB", 100, and "GB" as arguments, determine how many 500 MB videos can fit on a 100 GB hard drive.

# 1. number_of_videos(500, "MB", 100, "GB") should return 200.
# 2. number_of_videos(1, "TB", 10, "TB") should return "Invalid video unit".
# 3. number_of_videos(2000, "MB", 100000, "MB") should return "Invalid drive unit".
# 4. number_of_videos(500000, "KB", 2, "TB") should return 4000.
# 5. number_of_videos(1.5, "GB", 2.2, "TB") should return 1466.


def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    video_units = {"B": 1, "KB": 1000, "MB": 1000**2, "GB": 1000**3}
    drive_units = {"GB": 1000**3, "TB": 1000**4}

    if video_unit not in video_units:
        return "Invalid video unit"
    if drive_unit not in drive_units:
        return "Invalid drive unit"

    video_size_bytes = video_size * video_units[video_unit]
    drive_size_bytes = drive_size * drive_units[drive_unit]

    return int(drive_size_bytes // video_size_bytes)


print(number_of_videos(500, "MB", 100, "GB"))
print(number_of_videos(1, "TB", 10, "TB"))
print(number_of_videos(2000, "MB", 100000, "MB"))
print(number_of_videos(500000, "KB", 2, "TB"))
print(number_of_videos(1.5, "GB", 2.2, "TB"))