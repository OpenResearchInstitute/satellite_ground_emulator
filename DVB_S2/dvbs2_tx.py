#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dvbs2 Tx
# Generated: Tue Feb  9 10:45:24 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import dtv
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class dvbs2_tx(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Dvbs2 Tx")

        ##################################################
        # Variables
        ##################################################
        self.symbol_rate = symbol_rate = 5000000
        self.taps = taps = 100
        self.samp_rate = samp_rate = symbol_rate * 2
        self.rolloff = rolloff = 0.2
        self.frequency = frequency = 1280e6

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=frequency,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=True,
        	avg_alpha=0.13333,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, (firdes.root_raised_cosine(1.0, samp_rate, samp_rate/2, rolloff, taps)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.dtv_dvbs2_physical_cc_0 = dtv.dvbs2_physical_cc(dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.MOD_16APSK, dtv.PILOTS_ON, 0)
        self.dtv_dvbs2_modulator_bc_0 = dtv.dvbs2_modulator_bc(dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.MOD_16APSK, dtv.INTERPOLATION_OFF)
        self.dtv_dvbs2_interleaver_bb_0 = dtv.dvbs2_interleaver_bb(dtv.FECFRAME_NORMAL, dtv.C_OTHER, dtv.MOD_16APSK)
        self.dtv_dvb_ldpc_bb_0 = dtv.dvb_ldpc_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.MOD_OTHER)
        self.dtv_dvb_bch_bb_0 = dtv.dvb_bch_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10, )
        self.dtv_dvb_bbscrambler_bb_0 = dtv.dvb_bbscrambler_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10, )
        self.dtv_dvb_bbheader_bb_0 = dtv.dvb_bbheader_bb(dtv.STANDARD_DVBS2, dtv.FECFRAME_NORMAL, dtv.C9_10, dtv.RO_0_20, dtv.INPUTMODE_NORMAL, dtv.INBAND_OFF, 168, 4000000)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/Volumes/work/run/shm/adv16apsk910.ts", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.dtv_dvb_bbheader_bb_0, 0))    
        self.connect((self.dtv_dvb_bbheader_bb_0, 0), (self.dtv_dvb_bbscrambler_bb_0, 0))    
        self.connect((self.dtv_dvb_bbscrambler_bb_0, 0), (self.dtv_dvb_bch_bb_0, 0))    
        self.connect((self.dtv_dvb_bch_bb_0, 0), (self.dtv_dvb_ldpc_bb_0, 0))    
        self.connect((self.dtv_dvb_ldpc_bb_0, 0), (self.dtv_dvbs2_interleaver_bb_0, 0))    
        self.connect((self.dtv_dvbs2_interleaver_bb_0, 0), (self.dtv_dvbs2_modulator_bc_0, 0))    
        self.connect((self.dtv_dvbs2_modulator_bc_0, 0), (self.dtv_dvbs2_physical_cc_0, 0))    
        self.connect((self.dtv_dvbs2_physical_cc_0, 0), (self.fft_filter_xxx_0, 0))    
        self.connect((self.fft_filter_xxx_0, 0), (self.wxgui_fftsink2_0, 0))    

    def get_symbol_rate(self):
        return self.symbol_rate

    def set_symbol_rate(self, symbol_rate):
        self.symbol_rate = symbol_rate
        self.set_samp_rate(self.symbol_rate * 2)

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.fft_filter_xxx_0.set_taps((firdes.root_raised_cosine(1.0, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.fft_filter_xxx_0.set_taps((firdes.root_raised_cosine(1.0, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.fft_filter_xxx_0.set_taps((firdes.root_raised_cosine(1.0, self.samp_rate, self.samp_rate/2, self.rolloff, self.taps)))

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.wxgui_fftsink2_0.set_baseband_freq(self.frequency)


def main(top_block_cls=dvbs2_tx, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
