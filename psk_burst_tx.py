#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Psk Burst Tx
# Generated: Wed Oct 26 14:56:21 2016
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
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import burst
import es
import mapper
import pmt
import pyqt
import random
import sip
import sys


class psk_burst_tx(gr.top_block, Qt.QWidget):

    def __init__(self, pre_bits=[0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0]):
        gr.top_block.__init__(self, "Psk Burst Tx")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Psk Burst Tx")
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

        self.settings = Qt.QSettings("GNU Radio", "psk_burst_tx")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Parameters
        ##################################################
        self.pre_bits = pre_bits

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100e3
        
        
        self.ldpc_enc = ldpc_enc = fec.ldpc_encoder_make('/home/abraxas3d/goodies/share/gnuradio/fec/ldpc/271.127.3.112'); 

        ##################################################
        # Blocks
        ##################################################
        self.root_raised_cosine_filter_0 = filter.interp_fir_filter_ccf(2, firdes.root_raised_cosine(
        	1, 2.0, 1, 0.35, 41))
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	8192, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 0,0,1,0)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	8192, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 1,1)
        self.pyqt_meta_text_output_0 = pyqt.meta_text_output()
        self._pyqt_meta_text_output_0_win = self.pyqt_meta_text_output_0;
        self.top_layout.addWidget(self._pyqt_meta_text_output_0_win)
        self.pyqt_ctime_plot_0 = pyqt.ctime_plot('')
        self._pyqt_ctime_plot_0_win = self.pyqt_ctime_plot_0;
        self.top_grid_layout.addWidget(self._pyqt_ctime_plot_0_win, 1,0)
        self.mapper_mapper_msg_0 = mapper.mapper_msg(mapper.QPSK, ([0,1,3,2]))
        self.fec_async_encoder_0 = fec.async_encoder(ldpc_enc, False, True, True, 1500)
        self.es_source_0 = es.source(1*[gr.sizeof_gr_complex], 1, 2)
        self.channels_channel_model_0_0 = channels.channel_model(
        	noise_voltage=0.05,
        	frequency_offset=random.random()*1e-4,
        	epsilon=1.0+random.random()*1e-4,
        	taps=(1.0 + 1.0j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.burst_scheduler_0 = burst.burst_scheduler()
        self.burst_randomizer_0 = burst.randomizer(([0,14,15]), ([1,0,0,1,0,1,0,1,0,0,0,0,0,0,0]), 100000)
        self.burst_preamble_insert_0 = burst.preamble_insert((pre_bits))
        self.burst_padder_0 = burst.padder(144)
        self.burst_framer_0 = burst.framer(144)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_random_pdu_0 = blocks.random_pdu(50, 256/2, chr(0xFF), 2)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("TEST"), 1000)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, '/tmp/psk_ldpc_xmit.dat', False)
        self.blocks_file_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.blocks_random_pdu_0, 'generate'))    
        self.msg_connect((self.blocks_random_pdu_0, 'pdus'), (self.burst_framer_0, 'packed_pdus'))    
        self.msg_connect((self.burst_framer_0, 'unpacked_pdus'), (self.burst_padder_0, 'pdus'))    
        self.msg_connect((self.burst_padder_0, 'pdus'), (self.burst_randomizer_0, 'pdus'))    
        self.msg_connect((self.burst_preamble_insert_0, 'pdus'), (self.mapper_mapper_msg_0, 'pdus'))    
        self.msg_connect((self.burst_randomizer_0, 'pdus'), (self.fec_async_encoder_0, 'in'))    
        self.msg_connect((self.burst_scheduler_0, 'sched_pdu'), (self.es_source_0, 'schedule_event'))    
        self.msg_connect((self.burst_scheduler_0, 'sched_pdu'), (self.pyqt_meta_text_output_0, 'pdus'))    
        self.msg_connect((self.es_source_0, 'nproduced'), (self.burst_scheduler_0, 'nproduced'))    
        self.msg_connect((self.fec_async_encoder_0, 'out'), (self.burst_preamble_insert_0, 'pdus'))    
        self.msg_connect((self.mapper_mapper_msg_0, 'cpdus'), (self.burst_scheduler_0, 'sched_pdu'))    
        self.msg_connect((self.mapper_mapper_msg_0, 'cpdus'), (self.pyqt_ctime_plot_0, 'cpdus'))    
        self.connect((self.blocks_throttle_0, 0), (self.root_raised_cosine_filter_0, 0))    
        self.connect((self.channels_channel_model_0_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.channels_channel_model_0_0, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.channels_channel_model_0_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.es_source_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.root_raised_cosine_filter_0, 0), (self.channels_channel_model_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "psk_burst_tx")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_pre_bits(self):
        return self.pre_bits

    def set_pre_bits(self, pre_bits):
        self.pre_bits = pre_bits

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_ldpc_enc(self):
        return self.ldpc_enc

    def set_ldpc_enc(self, ldpc_enc):
        self.ldpc_enc = ldpc_enc


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    return parser


def main(top_block_cls=psk_burst_tx, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

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
