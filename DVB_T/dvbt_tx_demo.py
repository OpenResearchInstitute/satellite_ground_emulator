#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Dvbt Tx Demo
# Generated: Fri Feb 19 14:35:42 2016
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

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import dtv
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import sip
import sys
import time


class dvbt_tx_demo(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Dvbt Tx Demo")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Dvbt Tx Demo")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "dvbt_tx_demo")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = (8000000.0 * 8) / 7

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_waterfall_sink_x_1 = qtgui.waterfall_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	1269000000, #fc
        	samp_rate, #bw
        	"", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_1.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_1.enable_grid(False)
        
        if not True:
          self.qtgui_waterfall_sink_x_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_waterfall_sink_x_1.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_1.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_1.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_1.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_1_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	1269000000, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label("Relative Gain", "dB")
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(1269000000, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(14, 0)
        self.osmosdr_sink_0.set_if_gain(30, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.fft_vxx_0 = fft.fft_vcc(2048, False, (window.rectangular(2048)), True, 1)
        self.dtv_dvbt_symbol_inner_interleaver_0 = dtv.dvbt_symbol_inner_interleaver(1512, dtv.T2k, 1)
        self.dtv_dvbt_reference_signals_0 = dtv.dvbt_reference_signals(gr.sizeof_gr_complex, 1512, 2048, dtv.MOD_64QAM, dtv.NH, dtv.C2_3, dtv.C2_3, dtv.GI_1_32, dtv.T2k, 1, 0)
        self.dtv_dvbt_reed_solomon_enc_0 = dtv.dvbt_reed_solomon_enc(2, 8, 0x11d, 255, 239, 8, 51, 8)
        self.dtv_dvbt_map_0 = dtv.dvbt_map(1512, dtv.MOD_64QAM, dtv.NH, dtv.T2k, 1)
        self.dtv_dvbt_inner_coder_0 = dtv.dvbt_inner_coder(1, 1512, dtv.MOD_64QAM, dtv.NH, dtv.C2_3)
        self.dtv_dvbt_energy_dispersal_0 = dtv.dvbt_energy_dispersal(1)
        self.dtv_dvbt_convolutional_interleaver_0 = dtv.dvbt_convolutional_interleaver(136, 12, 17)
        self.dtv_dvbt_bit_inner_interleaver_0 = dtv.dvbt_bit_inner_interleaver(1512, dtv.MOD_64QAM, dtv.NH, dtv.T2k)
        self.digital_ofdm_cyclic_prefixer_0 = digital.ofdm_cyclic_prefixer(2048, 2048+64, 0, "")
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 2048)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.0022097087, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/Volumes/work/satellite_ground_emulator/DVB_S2/run/shm/adv16apsk910.ts", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.dtv_dvbt_energy_dispersal_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_waterfall_sink_x_1, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.digital_ofdm_cyclic_prefixer_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.dtv_dvbt_bit_inner_interleaver_0, 0), (self.dtv_dvbt_symbol_inner_interleaver_0, 0))    
        self.connect((self.dtv_dvbt_convolutional_interleaver_0, 0), (self.dtv_dvbt_inner_coder_0, 0))    
        self.connect((self.dtv_dvbt_energy_dispersal_0, 0), (self.dtv_dvbt_reed_solomon_enc_0, 0))    
        self.connect((self.dtv_dvbt_inner_coder_0, 0), (self.dtv_dvbt_bit_inner_interleaver_0, 0))    
        self.connect((self.dtv_dvbt_map_0, 0), (self.dtv_dvbt_reference_signals_0, 0))    
        self.connect((self.dtv_dvbt_reed_solomon_enc_0, 0), (self.dtv_dvbt_convolutional_interleaver_0, 0))    
        self.connect((self.dtv_dvbt_reference_signals_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.dtv_dvbt_reference_signals_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.dtv_dvbt_symbol_inner_interleaver_0, 0), (self.dtv_dvbt_map_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.digital_ofdm_cyclic_prefixer_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dvbt_tx_demo")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(1269000000, self.samp_rate)
        self.qtgui_waterfall_sink_x_1.set_frequency_range(1269000000, self.samp_rate)


def main(top_block_cls=dvbt_tx_demo, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
