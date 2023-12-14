"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        h7 = self.addHost( 'h7' )
        h8 = self.addHost( 'h8' )

        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )

        self.addLink( s1, h1)
        self.addLink( s1, h2)
        self.addLink( s2, h3)
        self.addLink( s2, h4)
        self.addLink( s2, h5)
        self.addLink( s3, h6)
        self.addLink( s3, h7)
        self.addLink( s3, h8)
        self.addLink( s1, s2)
        self.addLink( s2, s3)



topos = { 'mytopo': ( lambda: MyTopo() ) }
