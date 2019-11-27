# single list for all record types dictating field order

unified_list = [
    'NAME',
    'DESC',
    'ASG',
    'SCAN',
    'PINI',
    'PHAS',
    'EVNT',
    'TSE',
    'TSEL',
    'DTYP',
    'DISV',
    'DISA',
    'SDIS',
    'MLOK',
    'MLIS',
    'BKLNK',
    'DISP',
    'PROC',
    'STAT',
    'SEVR',
    'NSTA',
    'NSEV',
    'ACKS',
    'ACKT',
    'DISS',
    'LCNT',
    'PACT',
    'PUTF',
    'RPRO',
    'ASP',
    'PPN',
    'PPNR',
    'SPVT',
    'RSET',
    'DSET',
    'DPVT',
    'RDES',
    'LSET',
    'PRIO',
    'TPRO',
    'BKPT',
    'UDF',
    'UDFS',
    'TIME',
    'FLNK',
    'VAL',
    'OVAL',
    'INP',
    'MPST',
    'APST',
    'SIOL',
    'SVAL',
    'SIML',
    'SIMM',
    'SIMS',
    'OLDSIMM',
    'SSCN',
    'SDLY',
    'SIMPVT',
    'SIZV',
    'LEN',
    'OLEN',
    'DOL',
    'IVOA',
    'IVOV',
    'OMSL',
    'OUT',
    'SELM',
    'SELN',
    'SELL',
    'OFFS',
    'SHFT',
    'LNK0',
    'LNK1',
    'LNK2',
    'LNK3',
    'LNK4',
    'LNK5',
    'LNK6',
    'LNK7',
    'LNK8',
    'LNK9',
    'LNKA',
    'LNKB',
    'LNKC',
    'LNKD',
    'LNKE',
    'LNKF',
    'OLDN',
    'PREC',
    'DLY0',
    'DOL0',
    'DO0',
    'DLY1',
    'DOL1',
    'DO1',
    'DLY2',
    'DOL2',
    'DO2',
    'DLY3',
    'DOL3',
    'DO3',
    'DLY4',
    'DOL4',
    'DO4',
    'DLY5',
    'DOL5',
    'DO5',
    'DLY6',
    'DOL6',
    'DO6',
    'DLY7',
    'DOL7',
    'DO7',
    'DLY8',
    'DOL8',
    'DO8',
    'DLY9',
    'DOL9',
    'DO9',
    'DLYA',
    'DOLA',
    'DOA',
    'DLYB',
    'DOLB',
    'DOB',
    'DLYC',
    'DOLC',
    'DOC',
    'DLYD',
    'DOLD',
    'DOD',
    'DLYE',
    'DOLE',
    'DOE',
    'DLYF',
    'DOLF',
    'DOF',
    'CALC',
    'INPA',
    'INPB',
    'INPC',
    'INPD',
    'INPE',
    'INPF',
    'INPG',
    'INPH',
    'INPI',
    'INPJ',
    'INPK',
    'INPL',
    'EGU',
    'HOPR',
    'LOPR',
    'HIHI',
    'LOLO',
    'HIGH',
    'LOW',
    'HHSV',
    'LLSV',
    'HSV',
    'LSV',
    'AFTC',
    'AFVL',
    'HYST',
    'ADEL',
    'MDEL',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'LA',
    'LB',
    'LC',
    'LD',
    'LE',
    'LF',
    'LG',
    'LH',
    'LI',
    'LJ',
    'LK',
    'LL',
    'LALM',
    'ALST',
    'MLST',
    'RPCL',
    'DRVH',
    'DRVL',
    'NOBT',
    'RVAL',
    'ORAW',
    'MASK',
    'B0',
    'B1',
    'B2',
    'B3',
    'B4',
    'B5',
    'B6',
    'B7',
    'B8',
    'B9',
    'BA',
    'BB',
    'BC',
    'BD',
    'BE',
    'BF',
    'INAM',
    'LFLG',
    'SUBL',
    'SNAM',
    'ONAM',
    'SADR',
    'CADR',
    'BRSV',
    'EFLG',
    'INPM',
    'INPN',
    'INPO',
    'INPP',
    'INPQ',
    'INPR',
    'INPS',
    'INPT',
    'INPU',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'FTA',
    'FTB',
    'FTC',
    'FTD',
    'FTE',
    'FTF',
    'FTG',
    'FTH',
    'FTI',
    'FTJ',
    'FTK',
    'FTL',
    'FTM',
    'FTN',
    'FTO',
    'FTP',
    'FTQ',
    'FTR',
    'FTS',
    'FTT',
    'FTU',
    'NOA',
    'NOB',
    'NOC',
    'NOD',
    'NOE',
    'NOF',
    'NOG',
    'NOH',
    'NOI',
    'NOJ',
    'NOK',
    'NOL',
    'NOM',
    'NON',
    'NOO',
    'NOP',
    'NOQ',
    'NOR',
    'NOS',
    'NOT',
    'NOU',
    'NEA',
    'NEB',
    'NEC',
    'NED',
    'NEE',
    'NEF',
    'NEG',
    'NEH',
    'NEI',
    'NEJ',
    'NEK',
    'NEL',
    'NEM',
    'NEN',
    'NEO',
    'NEP',
    'NEQ',
    'NER',
    'NES',
    'NET',
    'NEU',
    'OUTA',
    'OUTB',
    'OUTC',
    'OUTD',
    'OUTE',
    'OUTF',
    'OUTG',
    'OUTH',
    'OUTI',
    'OUTJ',
    'OUTK',
    'OUTL',
    'OUTM',
    'OUTN',
    'OUTO',
    'OUTP',
    'OUTQ',
    'OUTR',
    'OUTS',
    'OUTT',
    'OUTU',
    'VALA',
    'VALB',
    'VALC',
    'VALD',
    'VALE',
    'VALF',
    'VALG',
    'VALH',
    'VALI',
    'VALJ',
    'VALK',
    'VALL',
    'VALM',
    'VALN',
    'VALO',
    'VALP',
    'VALQ',
    'VALR',
    'VALS',
    'VALT',
    'VALU',
    'OVLA',
    'OVLB',
    'OVLC',
    'OVLD',
    'OVLE',
    'OVLF',
    'OVLG',
    'OVLH',
    'OVLI',
    'OVLJ',
    'OVLK',
    'OVLL',
    'OVLM',
    'OVLN',
    'OVLO',
    'OVLP',
    'OVLQ',
    'OVLR',
    'OVLS',
    'OVLT',
    'OVLU',
    'FTVA',
    'FTVB',
    'FTVC',
    'FTVD',
    'FTVE',
    'FTVF',
    'FTVG',
    'FTVH',
    'FTVI',
    'FTVJ',
    'FTVK',
    'FTVL',
    'FTVM',
    'FTVN',
    'FTVO',
    'FTVP',
    'FTVQ',
    'FTVR',
    'FTVS',
    'FTVT',
    'FTVU',
    'NOVA',
    'NOVB',
    'NOVC',
    'NOVD',
    'NOVE',
    'NOVF',
    'NOVG',
    'NOVH',
    'NOVI',
    'NOVJ',
    'NOVK',
    'NOVL',
    'NOVM',
    'NOVN',
    'NOVO',
    'NOVP',
    'NOVQ',
    'NOVR',
    'NOVS',
    'NOVT',
    'NOVU',
    'NEVA',
    'NEVB',
    'NEVC',
    'NEVD',
    'NEVE',
    'NEVF',
    'NEVG',
    'NEVH',
    'NEVI',
    'NEVJ',
    'NEVK',
    'NEVL',
    'NEVM',
    'NEVN',
    'NEVO',
    'NEVP',
    'NEVQ',
    'NEVR',
    'NEVS',
    'NEVT',
    'NEVU',
    'ONVA',
    'ONVB',
    'ONVC',
    'ONVD',
    'ONVE',
    'ONVF',
    'ONVG',
    'ONVH',
    'ONVI',
    'ONVJ',
    'ONVK',
    'ONVL',
    'ONVM',
    'ONVN',
    'ONVO',
    'ONVP',
    'ONVQ',
    'ONVR',
    'ONVS',
    'ONVT',
    'ONVU',
    'ZNAM',
    'RPVT',
    'WDPT',
    'ZSV',
    'OSV',
    'COSV',
    'RBV',
    'ORBV',
    'MALM',
    'NELM',
    'INDX',
    'BUSY',
    'NORD',
    'BPTR',
    'ZRVL',
    'TWVL',
    'THVL',
    'FRVL',
    'FVVL',
    'SXVL',
    'SVVL',
    'EIVL',
    'NIVL',
    'TEVL',
    'ELVL',
    'TVVL',
    'TTVL',
    'FFVL',
    'ZRST',
    'ONST',
    'TWST',
    'THST',
    'FRST',
    'FVST',
    'SXST',
    'SVST',
    'EIST',
    'NIST',
    'TEST',
    'ELST',
    'TVST',
    'TTST',
    'FTST',
    'FFST',
    'ZRSV',
    'ONSV',
    'TWSV',
    'THSV',
    'FRSV',
    'FVSV',
    'SXSV',
    'SVSV',
    'EISV',
    'NISV',
    'TESV',
    'ELSV',
    'TVSV',
    'TTSV',
    'FTSV',
    'FFSV',
    'UNSV',
    'SDEF',
    'RES',
    'ALG',
    'BALG',
    'NSAM',
    'IHIL',
    'ILIL',
    'OFF',
    'NUSE',
    'OUSE',
    'SPTR',
    'WPTR',
    'CVB',
    'INX',
    'EPVT',
    'LABL',
    'WFLG',
    'OFLG',
    'HASH',
    'CSTA',
    'CMD',
    'ULIM',
    'LLIM',
    'WDTH',
    'SGNL',
    'SVL',
    'WDOG',
    'MCNT',
    'SDEL',
    'PVAL',
    'CLCV',
    'INAV',
    'INBV',
    'INCV',
    'INDV',
    'INEV',
    'INFV',
    'INGV',
    'INHV',
    'INIV',
    'INJV',
    'INKV',
    'INLV',
    'OUTV',
    'OOPT',
    'ODLY',
    'DOPT',
    'OCAL',
    'OCLV',
    'OEVT',
    'POVL',
    'ORPC',
    'FMT',
    'IVLS',
    'INP0',
    'INP1',
    'INP2',
    'INP3',
    'INP4',
    'INP5',
    'INP6',
    'INP7',
    'INP8',
    'INP9',
    'LINR',
    'EGUF',
    'EGUL',
    'AOFF',
    'ASLO',
    'SMOO',
    'ESLO',
    'EOFF',
    'ROFF',
    'PBRK',
    'INIT',
    'LBRK',
    'RARM',
    'OROC',
    'OIF',
    'OMOD',
    'NVL',
    'NLST'
]

unified_lookup_list = {
    field: index for field, index in enumerate(unified_list)
}
