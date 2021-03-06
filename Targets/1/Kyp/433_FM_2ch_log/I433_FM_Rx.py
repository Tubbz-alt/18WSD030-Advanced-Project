#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FM audio 433 RX
# Author: KD - 6/12/18
# Description: FM audio file Rx at 434 MHz
# Generated: Thu Jul 19 21:10:27 2007
##################################################

from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import gr, blocks
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import time


class I433_FM_Rx(gr.top_block):

    def __init__(self, freq=434e6, rx_gain=100):
        gr.top_block.__init__(self, "FM audio 433 RX")

        ##################################################
        # Parameters
        ##################################################
        self.freq = freq
        self.rx_gain = rx_gain

        ##################################################
        # Variables
        ##################################################
        self.server_port = server_port = 30000
        self.server_address = server_address = "192.168.10.2"
        self.samp_rate = samp_rate = 500e3
        self.lpf_decim = lpf_decim = 2
        self.audio_samp_rate = audio_samp_rate = 44.1e3

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(2),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec("A:A A:B", 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0.set_gain(rx_gain, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0.set_bandwidth(200e3, 0)
        self.uhd_usrp_source_0.set_center_freq(freq, 1)
        self.uhd_usrp_source_0.set_gain(rx_gain, 1)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 1)
        self.uhd_usrp_source_0.set_bandwidth(200e3, 1)
        (self.uhd_usrp_source_0).set_max_output_buffer(1000000)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(lpf_decim, firdes.low_pass(
        	1, samp_rate, 7e3, 7e3, firdes.WIN_HAMMING, 6.76))
        (self.low_pass_filter_0_0).set_max_output_buffer(1000000)
        self.low_pass_filter_0 = filter.fir_filter_ccf(lpf_decim, firdes.low_pass(
        	1, samp_rate, 7e3, 7e3, firdes.WIN_HAMMING, 6.76))
        (self.low_pass_filter_0).set_max_output_buffer(1000000)
        self.blocks_file_meta_sink_0_0 = blocks.file_meta_sink(gr.sizeof_gr_complex*1, "/home/root/grc_programs/Kyp/data/433_FM_ch1", samp_rate, 1, blocks.GR_FILE_FLOAT, True, 1000000, "", False)
        self.blocks_file_meta_sink_0_0.set_unbuffered(False)
        self.blocks_file_meta_sink_0 = blocks.file_meta_sink(gr.sizeof_gr_complex*1, "/home/root/grc_programs/Kyp/data/433_FM_nouse", samp_rate, 1, blocks.GR_FILE_FLOAT, True, 1000000, "", False)
        self.blocks_file_meta_sink_0.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.low_pass_filter_0, 0), (self.blocks_file_meta_sink_0_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.blocks_file_meta_sink_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.uhd_usrp_source_0, 1), (self.low_pass_filter_0_0, 0))    

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)
        self.uhd_usrp_source_0.set_center_freq(self.freq, 1)

    def get_rx_gain(self):
        return self.rx_gain

    def set_rx_gain(self, rx_gain):
        self.rx_gain = rx_gain
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 0)
        	
        self.uhd_usrp_source_0.set_gain(self.rx_gain, 1)
        	

    def get_server_port(self):
        return self.server_port

    def set_server_port(self, server_port):
        self.server_port = server_port

    def get_server_address(self):
        return self.server_address

    def set_server_address(self, server_address):
        self.server_address = server_address

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 7e3, 7e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 7e3, 7e3, firdes.WIN_HAMMING, 6.76))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_lpf_decim(self):
        return self.lpf_decim

    def set_lpf_decim(self, lpf_decim):
        self.lpf_decim = lpf_decim

    def get_audio_samp_rate(self):
        return self.audio_samp_rate

    def set_audio_samp_rate(self, audio_samp_rate):
        self.audio_samp_rate = audio_samp_rate


def argument_parser():
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option(
        "", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(434e6),
        help="Set freq [default=%default]")
    parser.add_option(
        "", "--rx-gain", dest="rx_gain", type="eng_float", default=eng_notation.num_to_str(100),
        help="Set rx_gain [default=%default]")
    return parser


def main(top_block_cls=I433_FM_Rx, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(freq=options.freq, rx_gain=options.rx_gain)
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
