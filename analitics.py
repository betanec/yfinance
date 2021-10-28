import pandas as pd
import numpy as np
import plotly.graph_objs as go
import csv
import yfinance as yf
import xlrd, xlwt


#старый подход
# tickers1 = ['LRC-USD', 'GNO-USD', 'MIR1-USD', 'CKB-USD', 'STORJ-USD', 'DAG-USD', 'SNT-USD', 'WAXP-USD', 'BCN-USD', 'STRAX-USD', 'RLC-USD', 'VTHO-USD', 'HNC-USD', 'TOMO-USD', 'REP-USD', 'BAND-USD', 'OXT-USD', 'ERG-USD', 'FET-USD', 'IOTX-USD', 'STEEM-USD', 'ARDR-USD', 'MCO-USD', 'NKN-USD', 'EWT-USD', 'FUN-USD', 'CVC-USD', 'META-USD', 'PHA-USD', 'SRM-USD', 'MLN-USD', 'ANT-USD', 'NU-USD', 'BAL-USD', 'HIVE-USD', 'ABBC-USD', 'SAPP-USD', 'MED-USD', 'ARK-USD', 'BTS-USD', 'ETN-USD', 'MTL-USD', 'WAN-USD', 'DIVI-USD', 'PAC-USD', 'XNC-USD', 'AVA-USD', 'PPT-USD', 'KMD-USD', 'VLX-USD', 'MONA-USD', 'BTM-USD', 'KIN-USD', 'COTI-USD', 'TWT-USD', 'NYE-USD', 'SYS-USD', 'WOZX-USD', 'REV-USD', 'DERO-USD', 'GAS-USD', 'IRIS-USD', 'HNS-USD', 'DNT-USD', 'NRG-USD', 'FIO-USD', 'DMCH-USD', 'RBTC-USD', 'TT-USD', 'AION-USD', 'SERO-USD', 'FIRO-USD', 'BURST-USD', 'XHV-USD', 'GRS-USD', 'SNM-USD', 'SBD-USD', 'RDD-USD', 'KDA-USD', 'ATRI-USD', 'ZNN-USD', 'CRU-USD', 'AXEL-USD', 'MWC-USD', 'BEAM-USD', 'ADX-USD', 'WTC-USD', 'LOKI-USD', 'APL-USD', 'VRA-USD', 'MASS-USD', 'ELA-USD', 'VSYS-USD', 'CET-USD', 'KRT-USD', 'NIM-USD', 'NULS-USD', 'SRK-USD', 'PIVX-USD', 'VERI-USD']
# # получим инфу по крипте, конкретный метод для гета сразу всех валют я не нашел и просто скопировал с HTML
# tickers2 = tickers1.split(',')#тут засплиитим по ",", чтобы с цикла вывести поочередно каждый item из списка


#новый подход
# tikers = ['BTC-USD', 'ETH-USD', 'USDT-USD', 'BNB-USD', 'ADA-USD', 'XRP-USD', 'USDC-USD', 'DOGE-USD', 'HEX-USD', 'DOT1-USD', 'UNI3-USD', 'BCH-USD', 'LTC-USD', 'SOL1-USD', 'LINK-USD', 'ETC-USD', 'MATIC-USD', 'XLM-USD', 'ICP1-USD', 'THETA-USD', 'VET-USD', 'FIL-USD', 'TRX-USD', 'XMR-USD', 'EOS-USD', 'AAVE-USD', 'CRO-USD', 'LUNA1-USD', 'SHIB-USD', 'ALGO-USD', 'ATOM1-USD', 'MKR-USD', 'BSV-USD', 'NEO-USD', 'COMP-USD', 'XTZ-USD', 'AMP1-USD', 'AVAX-USD', 'MIOTA-USD', 'GRT2-USD', 'CCXX-USD', 'STX1-USD', 'CHZ-USD', 'EGLD-USD', 'KSM-USD', 'BTT1-USD', 'TUSD-USD', 'TFUEL-USD', 'HBAR-USD', 'DCR-USD', 'WAVES-USD', 'RUNE-USD', 'CTC1-USD', 'CEL-USD', 'ZEC-USD', 'DASH-USD', 'MANA-USD', 'ENJ-USD', 'SNX-USD', 'YFI-USD', 'XEM-USD', 'HNT1-USD', 'XDC-USD', 'HOT1-USD', 'QNT-USD', 'SUSHI-USD', 'ONE2-USD', 'ZIL-USD', 'BAT-USD', 'BTG-USD', 'CELO-USD', 'BNT-USD', 'ZEN-USD', 'DFI-USD', 'XWC-USD', 'QTUM-USD', 'CRV-USD', 'ONT-USD', 'ZRX-USD', 'SC-USD', 'DGB-USD', 'NANO-USD', 'OMG-USD', 'UMA-USD', 'ICX-USD', 'ANKR-USD', 'RVN-USD', 'SAND-USD', 'VGX-USD', 'ARRR-USD', 'BCD-USD', 'AR-USD', 'IOST-USD', 'XVG-USD', 'LSK-USD', 'GLM-USD', 'MAID-USD', 'KNC-USD', 'LRC-USD', 'KAVA-USD', 'LRC-USD', 'чё', 'MIR1-USD', 'CKB-USD', 'STORJ-USD', 'DAG-USD', 'SNT-USD', 'WAXP-USD', 'BCN-USD', 'STRAX-USD', 'RLC-USD', 'VTHO-USD', 'HNC-USD', 'TOMO-USD', 'REP-USD', 'BAND-USD', 'OXT-USD', 'ERG-USD', 'FET-USD', 'IOTX-USD', 'STEEM-USD', 'ARDR-USD', 'MCO-USD', 'NKN-USD', 'EWT-USD', 'FUN-USD', 'CVC-USD', 'META-USD', 'PHA-USD', 'SRM-USD', 'MLN-USD', 'ANT-USD', 'NU-USD', 'BAL-USD', 'HIVE-USD', 'ABBC-USD', 'SAPP-USD', 'MED-USD', 'ARK-USD', 'BTS-USD', 'ETN-USD', 'MTL-USD', 'WAN-USD', 'DIVI-USD', 'PAC-USD', 'XNC-USD', 'AVA-USD', 'PPT-USD', 'KMD-USD', 'VLX-USD', 'MONA-USD', 'BTM-USD', 'KIN-USD', 'COTI-USD', 'TWT-USD', 'NYE-USD', 'SYS-USD', 'WOZX-USD', 'REV-USD', 'DERO-USD', 'GAS-USD', 'IRIS-USD', 'HNS-USD', 'DNT-USD', 'NRG-USD', 'FIO-USD', 'DMCH-USD', 'RBTC-USD', 'TT-USD', 'AION-USD', 'SERO-USD', 'FIRO-USD', 'BURST-USD', 'XHV-USD', 'GRS-USD', 'SNM-USD', 'SBD-USD', 'RDD-USD', 'KDA-USD', 'ATRI-USD', 'ZNN-USD', 'CRU-USD', 'AXEL-USD', 'MWC-USD', 'BEAM-USD', 'ADX-USD', 'WTC-USD', 'LOKI-USD', 'APL-USD', 'VRA-USD', 'MASS-USD', 'ELA-USD', 'VSYS-USD', 'CET-USD', 'KRT-USD', 'NIM-USD', 'NULS-USD', 'SRK-USD', 'PIVX-USD', 'VERI-USD', 'AE-USD', 'PLC-USD', 'NXS-USD', 'DGD-USD', 'WICC-USD', 'GXC-USD', 'PCX-USD', 'HC-USD', 'VTC-USD', 'CTXC-USD', 'MHC-USD', 'NAV-USD', 'MARO-USD', 'FSN-USD', 'PPC-USD', 'VITE-USD', 'QASH-USD', 'BEPRO-USD', 'GRIN-USD', 'PZM-USD', 'PAI-USD', 'CUT-USD', 'GO-USD', 'ZANO-USD', 'SOLVE-USD', 'DNA1-USD', 'NMC-USD', 'ZEL-USD', 'ADK-USD', 'SKY-USD', 'XSN-USD', 'NAS-USD', 'GBYTE-USD', 'PART-USD', 'SALT-USD', 'BIP-USD', 'NEBL-USD', 'WABI-USD', 'QRL-USD', 'GAME-USD', 'LBC-USD', 'GLEEC-USD', 'NXT-USD', 'VAL1-USD', 'RSTR-USD', 'FCT-USD', 'NLG-USD', 'BHP-USD', 'DCN-USD', 'ETP-USD', 'BTC2-USD', 'PAY-USD', 'NVT-USD', 'AEON-USD', 'BHD-USD', 'MRX-USD', 'TRUE-USD', 'VIA-USD', 'ZYN-USD', 'UBQ-USD', 'ACT-USD', 'LCC-USD', 'DYN-USD', 'HTML-USD', 'POA-USD', 'CMT1-USD', 'SFT-USD', 'BLOCK-USD', 'FLO-USD', 'HPB-USD', 'GHOST1-USD', 'DMD-USD', 'SMART-USD', 'WGR-USD', 'OBSR-USD', 'PMEER-USD', 'DTEP-USD', 'TRTL-USD', 'XMC-USD', 'SCC3-USD', 'VEX-USD', 'EMC2-USD', 'BTX-USD', 'HTDF-USD', 
# 'VITAE-USD', 'CHI-USD', 'AMB-USD', 'INSTAR-USD', 'ACH-USD', 'PI-USD', 'YOYOW-USD', 'MAN-USD', 'XDN-USD', 'FTC-USD', 'XMY-USD', 'TERA-USD', 'RINGX-USD', 'SNGLS-USD', 'PHR-USD', 'INT-USD', 'FO-USD', 'GRC-USD', 'MIR-USD', 'WINGS-USD', 
# 'IDNA-USD', 'USNBT-USD', 'QRK-USD', 'XST-USD', 'NYZO-USD', 'BLK-USD', 'SONO1-USD', 'ILC-USD', 'OTO-USD', 'VIN-USD', 'BPS-USD', 'MGO-USD', 'AYA-USD', 'CRW-USD', 'FAIR-USD', 'XLT-USD', 'GHOST-USD', 'CURE-USD', 'TUBE-USD', 'SCP-USD', 'XRC-USD', 'BCA-USD', 'DIME-USD', 'IOC-USD', 'COLX-USD', 'NIX-USD', 'GCC1-USD', 'DDK-USD', 'SUB-USD', 'BPC-USD', 'POLIS-USD', 'ERK-USD', 'XAS-USD', 'OWC-USD', 'XBY-USD', 'MBC-USD', 'EDG-USD', 'HYC-USD', 'OURO-USD', 'ATB-USD', 'FRST-USD', 'COMP1-USD', 'BDX-USD', 'BONO-USD', 'ECA-USD', 'ECC-USD', 'UNO-USD', 'CSC-USD', 'ALIAS-USD', 'NLC2-USD', 'LKK-USD', 'CLAM-USD', 'FLASH-USD', 'MOAC-USD', 'DUN-USD', 'XUC-USD', 'RBY-USD', 'MINT-USD', 'AIB-USD', 'DACC-USD', 'SPHR-USD', 'SHIFT-USD', 'JDC-USD', 'MIDAS-USD', 'MTC2-USD', 'CCA-USD', 'SLS-USD', 'DCY-USD', 'XCP-USD', 'LRG-USD', 'BRC-USD', 'GRN-USD', 'XCH-USD', 'BONFIRE-USD', 'VBK-USD', 'BST-USD']
rb = xlrd.open_workbook('C:\it\way\list_curr.xls', formatting_info=True)
#я просто импортивал данные в excel через URL используя 
#каунты и оффсеты: 100-0, 100-200, 100-300, 80-380
sheet = rb.sheet_by_index(0)
vals = [sheet.row_values(rownum) for rownum in range(380)]
tikers = [x for xs in vals for x in xs]
print(tikers)


def export_data(i):
    print(i)
    data = yf.download(tikers[i], period = '1d', interval = '15m')
    print(data)
    #тут сначала думал делать в одном файле, мб было правильно
    # with open('tickers2[i].csv') as filecsv: 
    #     writer = csv.writer(filecsv)
    #     line = tickers2[i]
    #     writer.writerow(line)
    df = pd.DataFrame(data)
    df.to_csv(str(tikers[i]) + '.csv')#импортим наши CSV с криптой


def vizualiztion(i): #несколько опасная штука, откроет графики в браузере в рендже 380, 
                    #поэтому открою всего 5, изначально думал тоже исользовать, но потом подумал, 
                    # что слишком долго дальше делать
    data = yf.download(tikers[i], period = '1d', interval = '15m')

    
    fig = go.Figure()

    
    fig.add_trace(go.Candlestick(x=data.index,
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'], name = 'market data'))

    # титульники
    fig.update_layout(
        title=str(tikers[i]) + '/' + 'live share price evolution',
        yaxis_title=str(tikers[i]))

    
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=6, label="6h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    #Show
    fig.show()


def counting():#делаем функцию, которая считает через цикл 
    #каждый элемент списка tikers и передает через переменную schetchik
    #значения в функции vizualization и export_data
    schetchick1 = 0
    schetchick2 = 0
    while schetchick1 != len(tikers):
        export_data(schetchick1)
        schetchick1 += 1
    while schetchick2 != len(tikers)-375:
        vizualiztion(schetchick2)
        schetchick2 += 1
counting()



