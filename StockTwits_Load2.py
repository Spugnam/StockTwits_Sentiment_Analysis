#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 00:03:02 2017

@author: Quentin
"""

import pandas as pd

from requestors import ST_BASE_PARAMS, ST_BASE_URL
from requestors import Requests as R


#ticker list US stock with Market Cap >1B
ticker_list1 = ["AAPL","GOOGL","GOOG","MSFT","FB","AMZN","CMCSA","INTC","CSCO","AMGN","CELG","KHC","AVGO","PCLN","NVDA","CHTR","GILD","WBA","TXN","SBUX","NFLX","QCOM","ADBE","PYPL","COST","MDLZ","BIDU","BIIB","TSLA","AMOV","TMUS","AABA","FOX","QQQ","ADP","REGN","ATVI","AMAT","CSX","CME","JD","CTSH","MAR","VRTX","EBAY","NXPI","EA","ESRX","INTU","FOXA","EQIX","ISRG","MU","ALXN","MNST","LBTYA","LBTYB","ADI","LBTYK","ILMN","DISH","INCY","FISV","CTRP","SIRI","AAL","LRCX","PCAR","AMTD","ADSK","WDC","NTES","EXPE","HBANO","ROST","CERN","NTRS","WLTW","VCSH","PAYX","FITB","TROW","MCHP","SWKS","PFF","INFO","ORLY","LBRDK","LBRDA","SYMC","MYL","CHKP","DLTR","DVY","SBAC","IBKR","VCIT","XLNX","BMRN","ULTA","LSXMK","VIA","HBAN","CTAS","HSIC","XRAY","KLAC","VRSK","ALGN","CA","IDXX","WFM","CINF","WYNN","VOD","NCLH","HAS","ACGL","MXIM","FAST","NDAQ","AMD","SHPG","CSJ","EMB","RYAAY","CTXS","NTAP","SNPS","MELI","ETFC","SNI","SHY","HOLX","QVCA","ASML","QVCB","EXPD","ANSS","MBB","LKQ","VIAB","CBOE","CDNS","CDW","VRSN","JBHT","STX","GRMN","SIVB","DOX","DISCB","YNDX","TRMB","CHRW","IBB","JAZZ","FANG","ZION","TTWO","OTEX","AGNCB","CSGP","CDK","VXUS","SEIC","SCZ","CGNX","DISCA","IPGP","FLEX","STLD","IEP","IAC","NWS","QRVO","LULU","ZG","EWBC","Z","SPLK","ALKS","DISCK","AKAM","JKHY","NWSA","GLPI","TEAM","ODFL","BHFWV","GT","MRVL","EXEL","BNDX","SSNC","MKTX","UHAL","FFIV","FWONK","WOOF","SBNY","TLT","NDSN","MIDD","JBLU","IEI","QGEN","TSCO","IEF","ACWI","CIU","CPRT","CG","ALNY","SGEN","ARCC","IXUS","AGNC","TSRO","SINA","LAMR","SRCL","ABMD","SPLS","ERIE","MAT","IONS","FTNT","HDS","KITE","BIVV","ON","PPC","COMM","PTC","DXCM","MOMO","MSCC","UTHR","LOGM","PBCT","CBSH","LOGI","PACW","ULTI","LECO","SATS","SHV","ATHN","ICLR","OZRK","VEON","BOKF","TRIP","RGLD","OLED","SABR","ESLT","NATI","ARRS","CACC","UBNT","COHR","FLIR","CONE","MSG","EEFT","FIZZ","LVNTA","BRCD","ZBRA","BBRY","FSLR","DNKN","PNFP","GNTX","MTCH","NUAN","LVNTB","HPT","SLM","NBIX","VNQI","CY","PRAH","ACHC","EXAS","PEGA","MDSO","LILA","POOL","WB","HAIN","SNH","PRXL","BRKR","LILAK","TFSL","IJT","MASI","FCNCA","BBBY","VWR","BPOP","IBKC","TECH","AZPN","WWD","BUFF","CASY","VMBS","BLKB","MPWR","WTFC","AKRX","MKSI","AAXJ","LPLA","AMCX","ISBC","LFUS","COLM","FHB","UMPQ","WINS","PTEN","CAVM","TECD","MEOH","TCBI","CDEV","ESGR","NAVI","HBHC","LOPE","BLUE","WEN","VSAT","PFPT","IART","UNIT","CLVS","MIK","PDCO","HCSG","VTIP","ACAD","JCOM","CBRL","UBSI","CRUS","BGCP","GOLD","LITE","STMP","HOMB","LSTR","PTLA","UMBF","ENTG","MORN","MBFI","OPK","MLCO","TXRH","ICUI","LANC","SLGN","CHFC","BANF","LNCE","NUVA","RP","ANAT","SFM","ILG","SAGE","NTNX","LEXEB","SGMS","IDTI","SBGI","HTHT","SLAB","LEXEA","PBYI","JUNO","FULT","CRTO","NKTR","PODD","AFSI","NICE","ODP","AVXS","ZNGA","SAFM","PDCE","NTCT","GRFS"]

ticker_list2 = ["MMYT","CATY","VIRT","MANH","CHDN","SIGI","INCR","AGIO","WAFD","PSEC","LIVN","LAUR","WMGI","NXST","FFIN","CMPR","PZZA","IRBT","YY","HQY","FCFS","RRR","ITRI","OLLI","AEIS","GWPH","FIVE","TREE","CVLT","HELE","JACK","GBCI","FNSR","CAR","SAVE","CACQ","WIX","KLXI","SANM","MTSI","RARE","MCHI","ICPT","ACWX","CBPO","MDCO","TSG","ACIW","BECN","DORM","LGND","FEYE","NEOG","PSMT","IUSG","ARLP","SMTC","WBMD","FMBI","BCPC","PLAY","ROLL","IDCC","CBSHP","SSB","PAAS","FGEN","SHOO","FV","FNGN","HAWK","VIAV","HOPE","ONCE","JJSF","MDRX","IBOC","CVBF","TTEK","TWOU","CREE","LPNT","IUSV","TSEM","VRNT","GRPN","IRWD","COLB","PRTA","MGEE","GLNG","PCTY","HA","MLNX","ONB","TIVO","URBN","IIVI","ROIC","COKE","FSV","SOHU","ABY","PEGI","ABCO","NGHC","OKTA","GSM","CSA","FOLD","WERN","EGBN","CAKE","TTD","TRMK","GPOR","MRCY","MATW","SRPT","ALGT","AMKR","ENDP","HSNI","SIR","FIBK","POWI","HZNP","SUPN","VCLT","MMSI","RDFN","AAAP","INOV","ERIC","MLHR","PLCE","QTEC","CSOD","DSGX","CCOI","VNOM","XOG","CBF","TOWN","ACXM","WSTC","AERI","PCH","UCBI","TWNK","CIGI","CFFN","INDB","SFBS","TQQQ","EXLS","BANR","LOXO","SKYW","BPMC","OMCL","YERR","UNFI","LTXB","BLDR","INGN","TTEC","RNST","PENN","CSQ","AAON","HALO","FELE","TERP","CZR","PINC","CENT","UPL","RDUS","GGAL","AGII","CCMP","PRAA","ALRM","EBIX","CALM","MGLN","TRUE","CENTA","GMLP","ETSY","GOV","SHEN","HTLD","PLXS","TELL","ACIA","IGF","BWLD","UFPI","FRME","SFNC","EXPO","ABCB","ORBK","IBTX","BOFI","QLYS","AMBA","MYGN","DGRW","SPNC","AHGP","WSBC","NAVG","AAWW","PRFZ","CORE","LXRX","VGSH","MDXG","NVCR","EUFN","AMED","NWBI","RUSHA","KALU","COUP","CORT","CALD","MANT","BGNE","NTRI","BLMN","FFBC","ISCA","SYNA","OTTR","HMSY","TBPH","SFLY","NSIT","AMWD","BATRK","BRKS","BL","FWRD","SYNT","MIME","MSTR","MNRO","NBTB","PAHC","CSFL","RUSHB","FEX","ERI","RMR","TVTY","NXTM","PRGS","SIMO","IOSP","SBRA","APOG","NTGR","GNCMA","CRED","PCRX","JOBS","OSIS","ATSG","IMPV","WDFC","OCLR","LORL","FOXF","PDP","PPBI","WABC","SCHL","SYKE","GPRO","RGEN","WSFS","HMHC","MINI","INVA","INFN","CYBR","AINV","RMBS","UBSH","AXDX","WPPGY","ARRY","CNMD","XLRN","KLIC","HTLF","BMCH","SCSS","LABL","TTMI","SAIA","FMI","WETF","SODA","BOBE","PKW","AAXN","FTSL","XPER","CSGS","CTRE","SMCI","SRUN","BSFT","GIII","STBA","BPFH","AIMC","CVGW","NOVT","VGIT","SPWR","GBT","NRCIB","USCR","ONEQ","PRIM","DIOD","SRCE","VONG","PLYA","MEDP","SSYS","NWLI","RAVN","CVCO","PATK","HYLS","AAOI","CATM","EGHT","PLUS","KRNY","MNTA","PSDO","EFII","IPAR","WEB","ATRI","OSUR","BZUN","TILE","APPF","INDY","JRVR","SEDG","IPXL","HUBG","LKFN","THRM","APPN","CENX","BABY","BNCL","XT","FIVN","CGBD","CAFD","BUSE","MB","VONV","GOGO","BRKL","ECOL","SNHY","EPAY","PNK","ASTE","UFCS","LHCG","DBVT","AMSF","GBDC","SOXX","HOLI","SAFT"]

ticker_list3 = ["DERM","ECPG","TRS","BEAT","IUSB","EGOV","ADTN","EIGI","AIMT","VTWO","FTXO","STBZ","QDEL","VREX","AOBC","CSTE","GTLS","ABAX","FTA","ESPR","VRNS","VECO","STFC","GHDX","SBCF","ISTB","XNCR","FTSM","IPCC","MITL","HLNE","LGIH","QSII","ENSG","SONC","SPTN","NDRM","CHCO","VWOB","BCOR","IRDM","SBSI","ATNI","GSK","NKE","UTX","UPS","ABEV","BBL","TD","SLB","SNP","BMY","MTU","LFC","LLY","GS","ATH","LEA","AVAL","BRFS","BWA","HII","GWW","CMG","PNW","LPL","EXR","IRM","ARMK","ACH","PRGO","FRT","TFX","DPZ","PVH","AOS","ROL","ALV","ECA","GPS","SQ","LUK","Y","LNT","WU","TMK","CC","TRGP","ATO","AFG","SCG","WLK","RGA","KKR","USB","DCM","MS","LMT","ABT","RIO","WBK","HDB","ACN","DEO","UNP","AGN","ITUB","BR","XEC","WGP","SNA","IEX","VAR","HBI","KT","INGR","CPL","VEEV","KIM","WPM","BPL","SPR","MBT","WES","NI","MTN","SEE","AER","LDOS","HOG","TSU","AYI","MAC","UGI","IPG","VER","TRU","WRB","AAP","AVY","AZUL","SHOP","PE","UAA","GOL","ZAYO","CLNS","LN","TWX","CVS","DOW","AXP","AZN","BNS","ING","DD","CCK","TKC","MOS","CPT","TTC","JWN","KEYS","NRG","YPF","ALLE","PHM","ST","WCG","OC","VOYA","LYV","H","ELS","CF","SBS","OAK","ZNH","EQGP","BERY","WBC","WUBA","LTM","AES","UA","WR","WPC","LII","MAN","GDDY","M","OGE","AIV","WAB","KSS","VST","ARW","PKI","PHI","HEI","PF","STE","CB","TMO","BLK","NEE","ENB","CAT","LOW","UBS","CRM","PNC","LYG","CL","PUK","BSBR","BBVA","STO","DUK","BBD","AIG","SUI","VIPS","W","PSO","KRC","AA","AXTA","RPM","BIO","GIL","GXP","XPO","TRQ","TER","EEP","JHX","ENBL","SPB","TOL","INVH","EVHC","HUBB","SCI","LEG","BKFS","PAC","ACC","CIT","FDS","FL","GGG","NYCB","LW","EOCC","TYL","WST","AM","ESRT","CBD","JEC","ASR","USFD","HLF","MIC","RL","DCI","HRB","SHI","CSL","OHI","HUN","LPT","BRO","EBR","OA","AR","BEP","FBR","EQM","BPY","ADNT","NNN","HTA","GGB","BC","GD","CNI","AMT","AMX","E","AMOV","MET","BBDO","PBR","TEF","SCHW","EPD","DHR","FDX","BK","COP","SMFG","SU","SYK","EOG","AET","MON","GM","VALE","SPG","HMC","SNE","RTN","ANTM","WTR","BURL","BRX","DEI","ICL","RNR","SERV","CFR","TX","AMH","FNFV","SMG","AIZ","RDY","KORS","AGCO","KAR","POST","FLR","PK","STWD","RICE","ALSN","G","JLL","UMC","ENLK","RHI","OSK","THO","PII","EV","DATA","NFX","LAZ","ATHM","JBL","PWR","AGO","TEO","ANDX","WSO","HFC","AXS","FAF","FLS","HP","ENIC","PSXP","WAL","CSRA","CPA","SNV","OLN","GWRE","RS","BWXT","VRX","TDY","DCT","DLB","HIW","ARD","KGC","CFX","MSG","ORI","NRZ","NEU","CPN","HPP","ATR","BMA","BAH","EPR","MDU","PTHN","HHC","NFG","SMI","VVC","CCJ","ABB","ITW","D","CUK","CCL","BMO","SO","LVS","PRU","OXY","NOC","BCS","RELX","ORAN","NGG","TJX","KMI","BDX","MFG","CI","TRP","PSX","KMB","F","RENX","SYT","BCE","BT","DE","CCI","COF","MFC","BX","RBS","BHGE","MMC","SON","HRC","RSPP","DFT","CCU","SHLX","ACM"]

ticker_list4 = ["EGN","DCP","SIX","ITCB","GRA","WBS","AVT","CX","RLGY","CRL","HXL","SNX","BFAM","MPW","RES","TARO","CLB","CAE","EXP","GDI","GPT","SC","VVV","CNK","MUR","PB","STOR","CR","GRUB","SFR","WEX","NCR","CUBE","RRC","FNB","SKX","FICO","UNVR","WFT","AL","WGL","CABO","CRI","IDA","ALR","EPAM","MTG","NTL","CTLT","CW","DKS","TRN","VR","THS","APU","DNB","WRI","GWR","MD","PAM","SIG","FHN","THG","PAH","WPX","PAYC","TDC","IGT","X","CHK","CPG","EPC","GPK","MNK","APLE","BWP","POR","MSM","SRC","JBGS","PAGP","AN","AQN","CS","EMR","BBT","CNQ","BABA","SPGI","CHA","ECL","ICE","WPZ","CAJ","BAM","NOK","VMW","DB","STZ","CM","PX","BSX","HAL","DAL","JCI","AON","EL","CHU","JNJ","INFY","TRV","PHG","STT","HUM","FMX","EXC","PCG","LYB","PSA","AEP","S","TLK","ALL","XOM","TRI","LUV","WM","ETN","NSC","JPM","PLD","HPQ","BAX","MCK","GIS","AFL","APD","TGT","SHW","VLO","ZTS","WIT","VET","USG","WSM","MMS","ASH","EME","TCP","TEGP","CNO","BCO","RYN","CAA","NS","OI","WTM","VSM","CUZ","EQC","OGS","ARES","BMS","R","TEX","CLGX","HR","HLS","SWX","PGRE","COR","AUO","AMGP","ERJ","RDN","SNDR","ALE","GSH","RBC","BKU","FUN","ESNT","PRI","AU","BKH","STAY","ITT","FLO","NJR","LM","PAG","GEL","NEA","OMF","DDR","FR","PSB","SR","SUN","CAB","SHO","HE","BOH","CNX","HGV","TEP","ASB","CIEN","RIG","TRCO","CIM","CHH","LPX","MTZ","CIG","DAN","TCO","COTV","SWFT","CNDT","GEO","INXN","TKR","VC","NYLD","NORD","JELD","SF","TWO","VMI","MOH","SXT","DLX","AVA","SID","USM","AAN","GEF","LSI","KEX","BSM","CMD","NUS","TPX","CBT","GHC","MCY","DST","HRG","LHO","PNM","GFI","MFA","B","FND","DOC","OFC","DNP","YELP","CXW","CTX","CLH","NHI","NYT","RPAI","RHP","TDS","CHE","PCI","WOR","ENS","CACI","ENLC","VLY","VAC","OUT","STL","NVG","SAIC","SUM","PRA","FIG","BVN","BDC","EVR","ELLI","NAV","TUP","VLP","IBA","KBH","MORE","REXR","TDOC","SCCO","FIS","IBN","SRE","CRH","HCA","HPE","FMS","TEL","MPC","STI","SYY","PGR","ETP","WFC","PPG","CMI","RACE","PPL","HCN","MT","GLW","CHT","YUM","AVB","CBS","EIX","RCL","WMB","VIV","VFC","ED","KEP","MTB","APC","BAC","WMT","DLPH","EQR","MCO","WY","EW","NWL","BEN","K","XEL","ROP","T","BUD","PG","V","ADM","ATUS","PKX","ZBH","SYF","APH","TTM","SLF","FCAU","VTR","FTV","BCR","PEG","PXD","GE","SHG","CP","DFS","TSN","DXC","IR","HSY","IP","KYO","AMP","CHL","TI","RSG","SWK","PH","CAH","KR","TU","IX","ROK","CCE","CVX","ORCL","HSBC","PFE","UAL","WDAY","NMR","TEVA","FCX","LVLT","RCI","DG","KB","HIG","HLT","OKE","WEC","KEY","TMHC","LPI","PDM","BDN","POL","RGC","AVX","BYD","EGP","KMT","RBA","SBGL","KNX","NWE","TEN","AHL","BXMT","UNF","MANU","MULE","NAD","TPL","ZEN","JBT","ORA","PFGC","TGNA","SBH","BFR","OSB","EXG","GMED","TSE","FII","CBU","PBH","STN","TCF","FCFS","BXS","EDR","JAG","TNET","CWH","MSA","DAR","BTU","SRG"]

ticker_list5 = ["UE","SJI","PEN","XON","WBT","WWW","PSTG","VGR","SWN","MUSA","BID","WTW","TWLO","CXP","HUBS","RNG","DY","QTS","DM","ABM","UFS","ESL","FDP","FUL","NGVT","RXN","RLJ","VSH","AXE","MDP","LAD","ASGN","PBF","OII","ENR","NOMD","STAG","SKT","KOS","WRE","WCC","AXON","RLI","AWI","LCII","GNRC","AKR","HTH","NEWR","TGS","BOX","KRO","RAD","BKD","HLI","KMPR","LXP","NVRO","AEL","GATX","IAG","MTX","CMP","KBR","PBI","APAM","MTDR","TR","WAGE","TREX","TROX","DRH","GWB","INT","HI","SEMG","AUY","HEP","AGI","PZE","PLNT","BITA","PEB","SEM","AB","CLF","ELP","WTS","AMFW","CLDR","KW","DOOR","SLCA","CVG","BIG","NAC","CLI","GME","KS","COT","CCP","LC","NUV","AIT","FSIC","GCP","MAIN","NEP","VNTR","CMC","DGI","NZF","EE","HAE","NBR","ROG","XHR","ALX","DSL","ERF","SSD","AMC","BGS","CPE","DDS","ADSW","GVA","JPS","PAY","ATGE","ALEX","AEO","RMP","SITE","CJ","KYN","LXFT","P","BLD","TPH","DECK","NNI","XRX","AF","AJRD","ATI","FCB","LTC","QUAD","VHI","VZ","NVS","KO","SSL","GGP","DTE","ES","Q","ABX","PFG","COL","A","NEM","BXP","EC","C","TSM","UNH","HD","ETE","DLR","MHK","NOW","PAA","BBY","NUE","MGM","OMC","CFG","PM","MRK","RF","HRL","BAP","DVN","MGA","ABC","CXO","EFX","RHT","SKM","CLX","APA","KOF","ESS","WCN","FDC","TM","DIS","UN","PEP","UL","TS","LNC","L","DPS","FNF","LH","VMC","CPB","BTI","FRC","SNAP","SNN","CNHI","MMP","O","ANDV","TV","FTS","POT","STM","NLSN","VNO","AZO","HRS","HCP","MA","BA","GPN","MTD","AME","MSI","COTY","TAP","MKL","TDG","QSR","BCH","DGX","SEP","WRK","AWK","CNA","FE","BLL","WAT","YUMC","AGR","CNC","HES","MBLY","BSMX","CAG","IVZ","IBM","AGU","AEE","ETR","HST","ANTX","DHI","SJM","LLL","BSAC","PBA","GIB","FLT","DOV","MLM","CE","VEDL","ADS","MPLX","FNV","ALB","TAL","CMS","COH","DVMT","NLY","TXT","TOT","SAP","MO","MCD","MMM","SNY","CMA","WHR","FTI","UGP","TECK","LEN","CLR","VNTV","CBG","NOV","CHD","EDU","LB","CNP","ANET","CTL","GPC","EMN","MAS","KMX","BP","PTR","MDT","ABBV","PANW","RJF","COO","TWTR","TSS","AEG","APO","MAA","MKC","TIF","IT","PNR","UNM","XL","COG","WF","FMC","REG","ARE","SQM","ENIA","NBL","DVA","ARNC","BHP","RY","NVO","HON","SAN","MRO","RE","KSU","MFCB","GG","EQT","ASX","BIP","XYL","JNPR","BG","WYN","IFF","RMD","AJG","ALK","CIB","CEA","ZTO","UHS","DRI","AEM","IHG","UDR","DRE","PKG","SJR","AMG","ALLY","CVE","BAK","HNP","SLG","MSCI","FBHS","NVR","URI","AAT","ARI","MDR","UTF","HYH","HL","GDOT","MWA","PRLB","YRD","CZZ","ARCO","CADE","CTB","CBM","GZT","KFY","OAS","QEP","LQ","MLI","WNS","NTB","CNS","CVA","WLL","AYR","CWT","IBP","NSR","TAC","AWR","CRS","IVR","NWN","FBC","GDV","KWR","ARCH","CPS","FGL","SCL","BEDU","BRC","EAT","DBD","MGP","REVG","SM","VG","MDC","SAM","FFG","FI","CEQP","HBM","MTH","NOAH","CARS","NSP","KRG","OMI","TRNO","TVPT","FRAC","NSM","OB"]

ticker_list6 = ["PRTY","AKS","AMN","ETY","PFS","CBI","DO","ENV","GNW","INN","LZB","MTOR","BDJ","JCP","THC","WPG","AIN","EVH","BHE","CVI","FOE","TAHO","WDR","BTT","ESV","WWE","DRQ","EVT","HNI","PVG","SPN","TPRE","HMN","PDI","AXL","MXL","QCP","SCS","TNH","BEL","CMCM","CCO","NPO","ESE","FN","DK","EEX","NBLX","OMAM","SMLP","QTWO","WD","DDD","CHSP","GLOB","MRC","MSGN","UVV","WNRL","FPF","GIMO","LADR","PLT","SFL","TGI","CBL","SSP","SPH","TYG","ADX","DSW","ATU","BHLB","CLS","FCPT","IPHI","BXMX","FLOW","BTZ","BBU","CO","EGO","HF","ITGR","DNOW","TGP","CHGG","EBS","NYRT","RDC","HYT","RQI","GNL","MEI","ADC","KAMN","TY","CDE","EIG","SFUN","WOW","BMI","FET","NP","OZM","BFS","TPC","FTAI","GAB","USNA","HOME","EDN","KN","TIME","GOLF","GLOG","DF","AYX","BBN","VLRS","HSC","ETG","MC","OR","ATKR","AZZ","SUPV","GTT","IMAX","CISN","CYS","EVTC","IRS","MATX","RWT","CUDA","CHS","HTZ","QUOT","RH","SSTK","SXI","CPK","FIT","PTY","SEAS","HCC","FCN","GBX","HRI","MBI","OIS","JOE","VSTO","AIR","ELY","FBP","OEC","TSLX","WMK","NFJ","AVP","ETW","FCF","NCS","RATE","EURN","GMS","FIX","GKOS","GPI","HASI","VCO","WRD","EEQ","MCRN","TRTN","AGRO","AAV","NGL","RVT","SWM","HESM","KREF","ACCO","TRTX","PGEM","TNC","JQC","NRK","BCC","CUB","DDC","EGL","CNNX","KRA","PKY","SHAK","YEXT","CVRR","GES","PMT","RMAX","SJW","SPXC","AWF","ABG","CAL","ELF","WGO","MYCC","DYN","PHK","WNC","WMS","APRN","CEO","FSS","MNR","JPC","RPT","VVI","CEM","USA","NMFC","ALG","HY","ARR","CSTM","HTGC","PUMP","UNT","BIF","CODI","WTTR","SMP","GTY","LL","OXM","WAIR","ZPIN","BANC","BLX","AG","UHT","ASIX","CPAC","MTL","GCI","AGX","MTW","HQH","FAX","BTG","CEF","CQH","CQP","LNG","EVV","FSP","GSAT","SIM","IMO","NGD","NG","PRK","UTG","SEB","SRCI","STRP","TXMD","TMP"]

def get_stock_stream(symbol, params={}):
    """ gets stream of messages for given symbol
        copied from api.py (found on GitHub)
    """
    all_params = ST_BASE_PARAMS.copy()
    return R.get_json(ST_BASE_URL + 'streams/symbol/{}.json'.format(symbol), params=all_params)


def capture_twits(ticker_list):
    '''
    Loads last 30 messages for all stocks in ticker_list 
    selects those with sentiment indicator (bullish/ bearish) 
    adds the messages to global variable twits_messages
    '''
    twits_messages = []
    id_list = []
    for ticker in ticker_list:
        my_stock_stream = get_stock_stream(ticker)
        try:
            print(ticker, 'Number of messages: ', len(my_stock_stream['messages']))
            for i in range(len(my_stock_stream['messages'])):
                if (my_stock_stream['messages'][i]['entities']['sentiment']!=None):  #only selects twits with indicators
                    if my_stock_stream['messages'][i]['id'] not in id_list: #avoid duplicates
                        dico = {'id': my_stock_stream['messages'][i]['id'], 
                                'body': my_stock_stream['messages'][i]['body'], 
                                'created_at': my_stock_stream['messages'][i]['created_at'],
                                'sentiment': my_stock_stream['messages'][i]['entities']['sentiment']['basic'],
                                'symbol': ticker,
                               'User Name': my_stock_stream['messages'][i]['user']['name'],
                               'username': my_stock_stream['messages'][i]['user']['username']}
                        twits_messages.append(dico)
                        id_list.append(my_stock_stream['messages'][i]['id'])
        except:
            pass
    print('Number of twits captured: ', len(twits_messages))
    #merge dictionnaries
    if len(twits_messages)>0:
        twits_to_add = pd.DataFrame(twits_messages)
        twits_to_add.sort_values('created_at', ascending=True, inplace=True)
        print('twits to add length', len(twits_to_add))
        twits_to_add.to_csv('twitstoadd.csv', encoding='utf-8', index=False)
        twits = pd.read_csv('twits.csv',encoding='utf-8')        
        print('Current twits file length: ', len(twits))
        twits3 = pd.concat([twits,twits_to_add])
        twits3.drop_duplicates(subset='id', keep='first', inplace=True)

        print('Total number of twits captured: ', len(twits3))
        twits3.to_csv('twits.csv', encoding='utf-8', index=False)
    

    
#Function to populate more twits to the twits DataFrame
import time

def twits_load(iterations, sleep_time):
    i=iterations
    while i>0:
        try:
            print("Initiating capture List1...")
            capture_twits(ticker_list1)
            print("Sleeping...")
            time.sleep(sleep_time)
            print("Initiating capture List2...")
            capture_twits(ticker_list2)
            print("Sleeping...")
            time.sleep(sleep_time)
            print("Initiating capture List3...")
            capture_twits(ticker_list3)
            print("Sleeping...")
            time.sleep(sleep_time)
            print("Initiating capture List4...")
            capture_twits(ticker_list4)
            print("Sleeping...")
            time.sleep(sleep_time)
            print("Initiating capture List5...")
            capture_twits(ticker_list5)
            print("Sleeping...")
            time.sleep(sleep_time)
            print("Initiating capture List6...")
            capture_twits(ticker_list6)
            print("Sleeping...")
            time.sleep(sleep_time)
  #store the dataframe to a file             
        except:
            print("Capture exception")
            pass
        print("****************Round completion: ", i)
        #print("Going to sleep...*****************************************")
        #time.sleep(sleep_time) #sleep for sleep_time seconds 
        i-=1
 
#capture_twits(ticker_list)

twits_load(10, 600)