These are some notes I took and some of the files I used when I hooked up a HackRF One
to my Linux server.

It assumes a working installation of GNU Radio to begin.

1. "Install HackRF Support in Linux.pdf" contains the steps I followed to add HackRF One
support to my GNU Radio installation

2. "fm_radio_rx.grc" is the flow graph I used to test the HackRF One support in
GNU radio.

3. "gstx.grc" and "gstx.py" are the flow graph and generated Python for a test thatn
transmits the a sample of DVB-S2 using the HackRF One. You'll have to change the path
of the source to point to the location of the "adv16apsk910.ts" containing the sample.
I had to tweak the properties of the "osmocom Sink" to remove the "bladerf=0" to get it
to work with my HackRF One.
I should be clear I get no credit for creating this flow graph. I got it from somebody
else and I don't know the original source.

4. "adv16apsk910.ts" contains a sample of DVB-S2 for test transmission. It was too big to upload to Github as a single file, so I split it up. You’ll have to reassemble it with something like “cat adv16apsk910.ts.* > adv16apsk910.ts”
