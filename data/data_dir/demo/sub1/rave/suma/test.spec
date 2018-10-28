# delimits comments

# Creation information:
#     user    : mbeauchamp
#     date    : Mon Sep 19 13:14:40 CDT 2011
#     machine : NBA-MB-iMac06.local
#     pwd     : /Volumes/data1/UT/IP/fs/SUMA
#     command : @SUMA_Make_Spec_FS -sid fs

# define the group
        Group = fs

# define various States
        StateDef = pial

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = lh.pial.asc
# Note that for RAVE to work, this path must be the absolute path; relative or no path does not work from within RAVE
	SurfaceVolume = /Volumes/data/Patrick/RAVE_OLD_BACKUP/YAB_Congruency1_vo/suma/fs_SurfVol_Alnd_Exp+orig
        SurfaceState = pial
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        FreeSurferSurface = rh.pial.asc
# Note that for RAVE to work, this path must be the absolute path; relative or no path does not work from within RAVE
	SurfaceVolume = /Volumes/data/Patrick/RAVE_OLD_BACKUP/YAB_Congruency1_vo/suma/fs_SurfVol_Alnd_Exp+orig
        SurfaceState = pial
        EmbedDimension = 3
        Anatomical = Y

NewSurface
        SurfaceFormat = ASCII
        SurfaceType = FreeSurfer
        SurfaceName = electrodes.asc
        Anatomical = Y
	Hemisphere = L

