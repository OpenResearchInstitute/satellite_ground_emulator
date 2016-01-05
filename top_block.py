#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Nov 23 16:23:36 2015
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio import vocoder
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from math import sqrt
from optparse import OptionParser
import sip
import sys
import time


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 400000
        self.preamble = preamble = [ -0.70711 + 0.70711j,   0.70711 - 0.70711j,  -0.70711 + 0.70711j,   0.70711 + 0.70711j,   0.70711 - 0.70711j,   0.70711 - 0.70711j,  -0.70711 + 0.70711j,  -0.70711 + 0.70711j, -0.70711 - 0.70711j,  -0.70711 - 0.70711j,   0.70711 - 0.70711j,   0.70711 + 0.70711j,  -0.70711 + 0.70711j,   0.70711 - 0.70711j,   0.70711 - 0.70711j,  -0.70711 + 0.70711j,  -0.70711 + 0.70711j,   0.70711 + 0.70711j,   0.70711 + 0.70711j,   0.70711 + 0.70711j,  -0.70711 - 0.70711j,  -0.70711 + 0.70711j,  -0.70711 + 0.70711j,  -0.70711 - 0.70711j,  -0.70711 - 0.70711j,   0.70711 - 0.70711j,   0.70711 + 0.70711j,  -0.70711 - 0.70711j,  -0.70711 - 0.70711j,   0.70711 - 0.70711j,   0.70711 + 0.70711j,  -0.70711 - 0.70711j,   0.70711 + 0.70711j,   0.70711 + 0.70711j,   0.70711 - 0.70711j,  -0.70711 + 0.70711j,   0.70711 + 0.70711j,  -0.70711 - 0.70711j,   0.70711 - 0.70711j,   0.70711 + 0.70711j]
        self.audio_rate = audio_rate = 8000
        self.audio_interp = audio_interp = 2
        self.voice_gain = voice_gain = 0
        self.tau = tau = 75e-6
        self.rx_channel = rx_channel = 110
        self.quadrature_rate = quadrature_rate = audio_rate*audio_interp
        self.qpsk_constellation = qpsk_constellation = digital.constellation_calcdist(([(sqrt(2)/2)+(sqrt(2)/2)*1j,-(sqrt(2)/2)+(sqrt(2)/2)*1j,(sqrt(2)/2)-(sqrt(2)/2)*1j,-(sqrt(2)/2)-(sqrt(2)/2)*1j]), (digital.psk_4()[1]), 4, 1).base()
        self.qpsk_constellation.gen_soft_dec_lut(8)
        self.preamble_size = preamble_size = len(preamble)
        
        self.poly_taps = poly_taps = firdes.low_pass(2.0, samp_rate, 20000, 1000, firdes.WIN_HAMMING, 6.76)
          
        self.payload_size = payload_size = 100
        self.num_channels = num_channels = 4
        self.max_deviation = max_deviation = 3500
        self.guard_size = guard_size = 10
        self.codec_rate = codec_rate = 64000
        self.bpsk_rate = bpsk_rate = 400000

        ##################################################
        # Blocks
        ##################################################
        self._voice_gain_range = Range(0, 2, 0.01, 0, 200)
        self._voice_gain_win = RangeWidget(self._voice_gain_range, self.set_voice_gain, "voice_gain", "counter_slider", float)
        self.top_layout.addWidget(self._voice_gain_win)
        self.tab2 = Qt.QTabWidget()
        self.tab2_widget_0 = Qt.QWidget()
        self.tab2_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab2_widget_0)
        self.tab2_grid_layout_0 = Qt.QGridLayout()
        self.tab2_layout_0.addLayout(self.tab2_grid_layout_0)
        self.tab2.addTab(self.tab2_widget_0, "Preamble Correlation")
        self.tab2_widget_1 = Qt.QWidget()
        self.tab2_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab2_widget_1)
        self.tab2_grid_layout_1 = Qt.QGridLayout()
        self.tab2_layout_1.addLayout(self.tab2_grid_layout_1)
        self.tab2.addTab(self.tab2_widget_1, "Received Analog Voice")
        self.top_grid_layout.addWidget(self.tab2, 1,1,1,1)
        self._rx_channel_options = (110, 110*2, 110*3, 0, )
        self._rx_channel_labels = ("0", "1", "2", "3", )
        self._rx_channel_group_box = Qt.QGroupBox("rx_channel")
        self._rx_channel_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._rx_channel_button_group = variable_chooser_button_group()
        self._rx_channel_group_box.setLayout(self._rx_channel_box)
        for i, label in enumerate(self._rx_channel_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._rx_channel_box.addWidget(radio_button)
        	self._rx_channel_button_group.addButton(radio_button, i)
        self._rx_channel_callback = lambda i: Qt.QMetaObject.invokeMethod(self._rx_channel_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._rx_channel_options.index(i)))
        self._rx_channel_callback(self.rx_channel)
        self._rx_channel_button_group.buttonClicked[int].connect(
        	lambda i: self.set_rx_channel(self._rx_channel_options[i]))
        self.top_layout.addWidget(self._rx_channel_group_box)
        self.vocoder_ulaw_decode_bs_0 = vocoder.ulaw_decode_bs()
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("serial=309AF9C", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(433e6, 0)
        self.uhd_usrp_source_0.set_gain(5, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.root_raised_cosine_filter_1 = filter.fir_filter_ccf(2, firdes.root_raised_cosine(
        	1, bpsk_rate, bpsk_rate/2, 0.35, 101))
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	bpsk_rate/2, #samp_rate
        	"Preamble Correlation", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
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
        self.tab2_layout_0.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_time_raster_sink_x_0_0 = qtgui.time_raster_sink_b(
        	codec_rate,
        	100,
        	(guard_size+payload_size)*num_channels,
        	([]),
        	([]),
        	"Received TDM Frame",
        	1,
        	)
        
        self.qtgui_time_raster_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_0.set_intensity_range(-1, 1)
        self.qtgui_time_raster_sink_x_0_0.enable_grid(False)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        colors = [2, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_raster_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_raster_sink_x_0_0_win, 1,2,1,1)
        self.qtgui_freq_sink_x_3 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	audio_rate, #bw
        	"Received Analog Voice", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_3.set_update_time(0.10)
        self.qtgui_freq_sink_x_3.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_3.enable_autoscale(False)
        self.qtgui_freq_sink_x_3.enable_grid(False)
        self.qtgui_freq_sink_x_3.set_fft_average(1.0)
        self.qtgui_freq_sink_x_3.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_3.disable_legend()
        
        if float == type(float()):
          self.qtgui_freq_sink_x_3.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_3.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_3_win = sip.wrapinstance(self.qtgui_freq_sink_x_3.pyqwidget(), Qt.QWidget)
        self.tab2_layout_1.addWidget(self._qtgui_freq_sink_x_3_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Received Spectrum", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 0,0,1,1)
        self.digital_map_bb_0_0 = digital.map_bb((digital.psk_4()[1]))
        self.digital_corr_est_cc_0 = digital.corr_est_cc((preamble), 1, 0, 0.15)
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(qpsk_constellation)
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(2)
        self.blocks_tagged_stream_align_0 = blocks.tagged_stream_align(gr.sizeof_gr_complex*1, "corr_start")
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 2000)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((voice_gain, ))
        self.blocks_keep_m_in_n_1 = blocks.keep_m_in_n(gr.sizeof_char, payload_size, num_channels*(payload_size+guard_size), rx_channel)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, num_channels*(payload_size+guard_size)/2, num_channels*(payload_size+guard_size)/2 + preamble_size, preamble_size)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 2*(num_channels*(payload_size+guard_size)/2+preamble_size)-1)
        self.audio_sink_0 = audio.sink(8000, "", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_delay_0, 0), (self.blocks_keep_m_in_n_0, 0))    
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))    
        self.connect((self.blocks_keep_m_in_n_1, 0), (self.vocoder_ulaw_decode_bs_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_keep_m_in_n_1, 0))    
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.qtgui_time_raster_sink_x_0_0, 0))    
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_short_to_float_0, 0), (self.qtgui_freq_sink_x_3, 0))    
        self.connect((self.blocks_tagged_stream_align_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))    
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.digital_map_bb_0_0, 0))    
        self.connect((self.digital_corr_est_cc_0, 0), (self.blocks_tagged_stream_align_0, 0))    
        self.connect((self.digital_corr_est_cc_0, 1), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.digital_map_bb_0_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))    
        self.connect((self.root_raised_cosine_filter_1, 0), (self.digital_corr_est_cc_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.root_raised_cosine_filter_1, 0))    
        self.connect((self.vocoder_ulaw_decode_bs_0, 0), (self.blocks_short_to_float_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble
        self.set_preamble_size(len(self.preamble))

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.set_quadrature_rate(self.audio_rate*self.audio_interp)
        self.qtgui_freq_sink_x_3.set_frequency_range(0, self.audio_rate)

    def get_audio_interp(self):
        return self.audio_interp

    def set_audio_interp(self, audio_interp):
        self.audio_interp = audio_interp
        self.set_quadrature_rate(self.audio_rate*self.audio_interp)

    def get_voice_gain(self):
        return self.voice_gain

    def set_voice_gain(self, voice_gain):
        self.voice_gain = voice_gain
        self.blocks_multiply_const_vxx_0.set_k((self.voice_gain, ))

    def get_tau(self):
        return self.tau

    def set_tau(self, tau):
        self.tau = tau

    def get_rx_channel(self):
        return self.rx_channel

    def set_rx_channel(self, rx_channel):
        self.rx_channel = rx_channel
        self._rx_channel_callback(self.rx_channel)
        self.blocks_keep_m_in_n_1.set_offset(self.rx_channel)

    def get_quadrature_rate(self):
        return self.quadrature_rate

    def set_quadrature_rate(self, quadrature_rate):
        self.quadrature_rate = quadrature_rate

    def get_qpsk_constellation(self):
        return self.qpsk_constellation

    def set_qpsk_constellation(self, qpsk_constellation):
        self.qpsk_constellation = qpsk_constellation

    def get_preamble_size(self):
        return self.preamble_size

    def set_preamble_size(self, preamble_size):
        self.preamble_size = preamble_size
        self.blocks_delay_0.set_dly(2*(self.num_channels*(self.payload_size+self.guard_size)/2+self.preamble_size)-1)
        self.blocks_keep_m_in_n_0.set_offset(self.preamble_size)
        self.blocks_keep_m_in_n_0.set_n(self.num_channels*(self.payload_size+self.guard_size)/2 + self.preamble_size)

    def get_poly_taps(self):
        return self.poly_taps

    def set_poly_taps(self, poly_taps):
        self.poly_taps = poly_taps

    def get_payload_size(self):
        return self.payload_size

    def set_payload_size(self, payload_size):
        self.payload_size = payload_size
        self.blocks_delay_0.set_dly(2*(self.num_channels*(self.payload_size+self.guard_size)/2+self.preamble_size)-1)
        self.blocks_keep_m_in_n_0.set_m(self.num_channels*(self.payload_size+self.guard_size)/2)
        self.blocks_keep_m_in_n_0.set_n(self.num_channels*(self.payload_size+self.guard_size)/2 + self.preamble_size)
        self.blocks_keep_m_in_n_1.set_m(self.payload_size)
        self.blocks_keep_m_in_n_1.set_n(self.num_channels*(self.payload_size+self.guard_size))
        self.qtgui_time_raster_sink_x_0_0.set_num_cols((self.guard_size+self.payload_size)*self.num_channels)

    def get_num_channels(self):
        return self.num_channels

    def set_num_channels(self, num_channels):
        self.num_channels = num_channels
        self.blocks_delay_0.set_dly(2*(self.num_channels*(self.payload_size+self.guard_size)/2+self.preamble_size)-1)
        self.blocks_keep_m_in_n_0.set_m(self.num_channels*(self.payload_size+self.guard_size)/2)
        self.blocks_keep_m_in_n_0.set_n(self.num_channels*(self.payload_size+self.guard_size)/2 + self.preamble_size)
        self.blocks_keep_m_in_n_1.set_n(self.num_channels*(self.payload_size+self.guard_size))
        self.qtgui_time_raster_sink_x_0_0.set_num_cols((self.guard_size+self.payload_size)*self.num_channels)

    def get_max_deviation(self):
        return self.max_deviation

    def set_max_deviation(self, max_deviation):
        self.max_deviation = max_deviation

    def get_guard_size(self):
        return self.guard_size

    def set_guard_size(self, guard_size):
        self.guard_size = guard_size
        self.blocks_delay_0.set_dly(2*(self.num_channels*(self.payload_size+self.guard_size)/2+self.preamble_size)-1)
        self.blocks_keep_m_in_n_0.set_m(self.num_channels*(self.payload_size+self.guard_size)/2)
        self.blocks_keep_m_in_n_0.set_n(self.num_channels*(self.payload_size+self.guard_size)/2 + self.preamble_size)
        self.blocks_keep_m_in_n_1.set_n(self.num_channels*(self.payload_size+self.guard_size))
        self.qtgui_time_raster_sink_x_0_0.set_num_cols((self.guard_size+self.payload_size)*self.num_channels)

    def get_codec_rate(self):
        return self.codec_rate

    def set_codec_rate(self, codec_rate):
        self.codec_rate = codec_rate

    def get_bpsk_rate(self):
        return self.bpsk_rate

    def set_bpsk_rate(self, bpsk_rate):
        self.bpsk_rate = bpsk_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.bpsk_rate/2)
        self.root_raised_cosine_filter_1.set_taps(firdes.root_raised_cosine(1, self.bpsk_rate, self.bpsk_rate/2, 0.35, 101))


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
