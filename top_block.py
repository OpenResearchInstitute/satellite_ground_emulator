#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Oct 17 14:33:20 2015
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
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from math import sqrt
from optparse import OptionParser
import numpy
import sip
import sys


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
        self.symb_rate = symb_rate = 500000
        self.samp_rate = samp_rate = 4000000
        self.voice_vol = voice_vol = 1
        self.samps_per_symb = samps_per_symb = samp_rate / symb_rate
        self.noise_var = noise_var = 0
        self.analog_cent_freq = analog_cent_freq = 1.25e6

        ##################################################
        # Blocks
        ##################################################
        self._voice_vol_range = Range(0, 10, 0.1, 1, 200)
        self._voice_vol_win = RangeWidget(self._voice_vol_range, self.set_voice_vol, "voice_vol", "counter_slider", float)
        self.top_layout.addWidget(self._voice_vol_win)
        self._noise_var_range = Range(0, 0.25, 0.01, 0, 200)
        self._noise_var_win = RangeWidget(self._noise_var_range, self.set_noise_var, "noise_var", "counter_slider", float)
        self.top_layout.addWidget(self._noise_var_win)
        self._analog_cent_freq_range = Range(0, 2e6, 0.1e6, 1.25e6, 200)
        self._analog_cent_freq_win = RangeWidget(self._analog_cent_freq_range, self.set_analog_cent_freq, "analog_cent_freq", "counter_slider", float)
        self.top_layout.addWidget(self._analog_cent_freq_win)
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=1,
                decimation=samp_rate / 32000,
                taps=None,
                fractional_bw=None,
        )
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=samp_rate / 8000,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_freq_sink_x_1_0_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate / 500, #bw
        	"Distorted Received", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_1_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_1_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_1_0_0.disable_legend()
        
        if float == type(float()):
          self.qtgui_freq_sink_x_1_0_0.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_0_win, 2,2,2,2)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Original BPSK (Complex)", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_1_0.set_fft_average(0.05)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_1_0.disable_legend()
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_1_0.set_plot_pos_half(not True)
        
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
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_win, 0,0,2,2)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Combined and Limited (Real)", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(True)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if float == type(float()):
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 2,0,2,2)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	8000, #bw
        	"Original Voice (Real)", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(True)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if float == type(float()):
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
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0,2,2,2)
        self.low_pass_filter_0 = filter.fir_filter_fff(4, firdes.low_pass(
        	1, 32000, 4000, 100, firdes.WIN_BLACKMAN, 6.76))
        self.hilbert_fc_0 = filter.hilbert_fc(64, firdes.WIN_HAMMING, 6.76)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc(([1/sqrt(2)+1j/sqrt(2),1/sqrt(2)-1j/sqrt(2),-1/sqrt(2)+1j/sqrt(2),-1/sqrt(2)-1j/sqrt(2)]), 1)
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(256, True)
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/hume/Desktop/AMSATDemos/NeroSoundTrax_test3_PCM_Mono_CBR_8SS_8000Hz.wav", True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, samps_per_symb)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(2, gr.GR_MSB_FIRST)
        self.blocks_multiply_xx_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((voice_vol, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((1, ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, samps_per_symb/2)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1, ))
        self.audio_sink_0 = audio.sink(8000, "", True)
        self.analog_sig_source_x_1_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, analog_cent_freq, 1.0/5.0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, -analog_cent_freq, 1, 0)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 1000000)), True)
        self.analog_rail_ff_0 = analog.rail_ff(-1, 1)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise_var, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 0))    
        self.connect((self.analog_rail_ff_0, 0), (self.blocks_add_xx_1, 1))    
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.analog_sig_source_x_1_1, 0), (self.blocks_multiply_xx_2, 1))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_2, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_add_xx_1, 0), (self.hilbert_fc_0, 0))    
        self.connect((self.blocks_add_xx_1, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_freq_sink_x_1_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.blocks_multiply_xx_2, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.blocks_complex_to_float_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.analog_rail_ff_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_multiply_const_vxx_1, 0))    
        self.connect((self.dc_blocker_xx_0, 0), (self.qtgui_freq_sink_x_1_0_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.hilbert_fc_0, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.low_pass_filter_0, 0), (self.dc_blocker_xx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_symb_rate(self):
        return self.symb_rate

    def set_symb_rate(self, symb_rate):
        self.symb_rate = symb_rate
        self.set_samps_per_symb(self.samp_rate / self.symb_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samps_per_symb(self.samp_rate / self.symb_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1_1.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate / 500)

    def get_voice_vol(self):
        return self.voice_vol

    def set_voice_vol(self, voice_vol):
        self.voice_vol = voice_vol
        self.blocks_multiply_const_vxx_1.set_k((self.voice_vol, ))

    def get_samps_per_symb(self):
        return self.samps_per_symb

    def set_samps_per_symb(self, samps_per_symb):
        self.samps_per_symb = samps_per_symb
        self.blocks_delay_0.set_dly(self.samps_per_symb/2)

    def get_noise_var(self):
        return self.noise_var

    def set_noise_var(self, noise_var):
        self.noise_var = noise_var
        self.analog_noise_source_x_0.set_amplitude(self.noise_var)

    def get_analog_cent_freq(self):
        return self.analog_cent_freq

    def set_analog_cent_freq(self, analog_cent_freq):
        self.analog_cent_freq = analog_cent_freq
        self.analog_sig_source_x_0.set_frequency(-self.analog_cent_freq)
        self.analog_sig_source_x_1_1.set_frequency(self.analog_cent_freq)


def main(top_block_cls=top_block, options=None):

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
