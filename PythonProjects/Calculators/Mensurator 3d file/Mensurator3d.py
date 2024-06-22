def mensurator3d () :

    #%% imports 

    import tkinter as gfx
    import math as m


    #%% base screen

    mensurator3dhome = gfx.Tk ()
    mensurator3dhome.configure ( bg = '#222222')

    Lintro = gfx.Label ( mensurator3dhome, text = '3D-Mensurator\nBy Ashwin Sharma',\
                        bg = '#C0FF02', fg = '#111111',\
                        font = ('courier', 12),\
                        bd = 2, relief = 'raised' )
    Lintro.grid ( column = 1 , row = 1 )




    #%% definitions

    def cube () :
        cubehome = gfx.Tk ()
        cubehome.configure (bg = '#222222')

        def vol () :
            cubevol = gfx.Tk ()
            cubevol.configure(bg = '#222222')

            Ledge = gfx.Label ( cubevol, text = 'ENter the edge',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Ledge.grid ( column = 1, row = 1 )

            Eedge = gfx.Entry ( cubevol,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Eedge.grid ( column = 1, row = 2)

            def Done () :
                edge = float ( Eedge.get () )
                vol = edge**3

                Lans = gfx.Label ( cubevol, text = str(str(vol)+ ' is the volume'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 4 )


            Dbut = gfx.Button ( cubevol, text = 'Done', command = Done, bg = '#222222', fg = '#C0FF02', bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 3)
        
        def csa () :
            cubecsa = gfx.Tk ()
            cubecsa.configure(bg = '#222222')

            Ledge = gfx.Label ( cubecsa, text = 'ENter the edge',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Ledge.grid ( column = 1, row = 1 )

            Eedge = gfx.Entry ( cubecsa,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Eedge.grid ( column = 1, row = 2)

            def Done () :
                edge = float ( Eedge.get () )
                csa = (edge**2)*6

                Lans = gfx.Label ( cubecsa, text = str(str(csa)+ ' is the CSA'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 4 )


            Dbut = gfx.Button ( cubecsa, text = 'Done', command = Done, bg = '#222222', fg = '#C0FF02', bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 3)

        def lsa () :
            cubelsa = gfx.Tk ()
            cubelsa.configure(bg = '#222222')

            Ledge = gfx.Label ( cubelsa, text = 'ENter the edge',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Ledge.grid ( column = 1, row = 1 )

            Eedge = gfx.Entry ( cubelsa,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Eedge.grid ( column = 1, row = 2)

            def Done () :
                edge = float ( Eedge.get () )
                lsa = (edge**2)*4

                Lans = gfx.Label ( cubelsa, text = str(str(lsa)+ ' is the LSA'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 4 )


            Dbut = gfx.Button ( cubelsa, text = 'Done', command = Done, bg = '#222222', fg = '#C0FF02', bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 3)
        
        
        Bvol = gfx.Button ( cubehome, command = vol, text = 'Find Volume',\
                            bg = '#222222', fg = '#C0FF02',\
                            bd = 2, relief = 'raised' )
        Bvol.grid ( column = 1, row = 1 )

        Bcsa = gfx.Button ( cubehome, command = csa, text = 'Find CSA',\
                            bg = '#222222', fg = '#C0FF02',\
                            bd = 2, relief = 'raised' )
        Bcsa.grid ( column = 1, row = 2 )

        Blsa = gfx.Button ( cubehome, command = lsa, text = 'Find LSA',\
                            bg = '#222222', fg = '#C0FF02',\
                            bd = 2, relief = 'raised' )
        Blsa.grid ( column = 1, row = 3 )

    def cuboid () :
        cuboidhome = gfx.Tk ()
        cuboidhome.configure(bg = '#222222')

        def vol () :

            cuboidvol = gfx.Tk()
            cuboidvol.configure (bg = '#222222')


            Llen = gfx.Label ( cuboidvol, text = 'ENter the length',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Llen.grid ( column=1,row=1)

            Elen = gfx.Entry ( cuboidvol,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Elen.grid ( column = 1, row=2)

            Lbdh = gfx.Label ( cuboidvol, text = 'ENter the breadth',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lbdh.grid ( column=1,row=3)

            Ebdh = gfx.Entry ( cuboidvol,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ebdh.grid ( column = 1, row=4)

            Lhei = gfx.Label ( cuboidvol, text = 'ENter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column=1,row=5)

            Ehei = gfx.Entry ( cuboidvol,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row=6)

            def Done () :
                lgh = float ( Elen.get () )
                bdh = float ( Ebdh.get () )
                hei = float ( Ehei.get () )

                volume = lgh*bdh*hei

                Lans = gfx.Label ( cuboidvol, text = str( str(volume)+' is the volume'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 8 )

            Dbut = gfx.Button ( cuboidvol, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 9)

        def csa () :
            cuboidcsa = gfx.Tk()
            cuboidcsa.configure (bg = '#222222')


            Llen = gfx.Label ( cuboidcsa, text = 'ENter the length',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Llen.grid ( column=1,row=1)

            Elen = gfx.Entry ( cuboidcsa,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Elen.grid ( column = 1, row=2)

            Lbdh = gfx.Label ( cuboidcsa, text = 'ENter the breadth',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lbdh.grid ( column=1,row=3)

            Ebdh = gfx.Entry ( cuboidcsa,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ebdh.grid ( column = 1, row=4)

            Lhei = gfx.Label ( cuboidcsa, text = 'ENter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column=1,row=5)

            Ehei = gfx.Entry ( cuboidcsa,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row=6)

            def Done () :
                lgh = float ( Elen.get () )
                bdh = float ( Ebdh.get () )
                hei = float ( Ehei.get () )

                csa = (2*lgh*bdh)+(2*bdh*hei)+(2*lgh*hei)

                Lans = gfx.Label ( cuboidcsa, text = str( str(csa)+' is the csa'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 8 )

            Dbut = gfx.Button ( cuboidcsa, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 9)

        def lsa_l () :
            cuboidlsa_l = gfx.Tk()
            cuboidlsa_l.configure (bg = '#222222')


            Llen = gfx.Label ( cuboidlsa_l, text = 'ENter the length',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Llen.grid ( column=1,row=1)

            Elen = gfx.Entry ( cuboidlsa_l,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Elen.grid ( column = 1, row=2)

            Lbdh = gfx.Label ( cuboidlsa_l, text = 'ENter the breadth',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lbdh.grid ( column=1,row=3)

            Ebdh = gfx.Entry ( cuboidlsa_l,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ebdh.grid ( column = 1, row=4)

            Lhei = gfx.Label ( cuboidlsa_l, text = 'ENter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column=1,row=5)

            Ehei = gfx.Entry ( cuboidlsa_l,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row=6)

            def Done () :
                lgh = float ( Elen.get () )
                bdh = float ( Ebdh.get () )
                hei = float ( Ehei.get () )

                lsa_l = (2*lgh*hei) + 2*(lgh*bdh)

                Lans = gfx.Label ( cuboidlsa_l, text = str( str(lsa_l)+' is the lsa_l'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 8 )

            Dbut = gfx.Button ( cuboidlsa_l, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 9)

        def lsa_b () :
            cuboidlsa_b = gfx.Tk()
            cuboidlsa_b.configure (bg = '#222222')


            Llen = gfx.Label ( cuboidlsa_b, text = 'ENter the length',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Llen.grid ( column=1,row=1)

            Elen = gfx.Entry ( cuboidlsa_b,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Elen.grid ( column = 1, row=2)

            Lbdh = gfx.Label ( cuboidlsa_b, text = 'ENter the breadth',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lbdh.grid ( column=1,row=3)

            Ebdh = gfx.Entry ( cuboidlsa_b,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ebdh.grid ( column = 1, row=4)

            Lhei = gfx.Label ( cuboidlsa_b, text = 'ENter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column=1,row=5)

            Ehei = gfx.Entry ( cuboidlsa_b,\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row=6)

            def Done () :
                lgh = float ( Elen.get () )
                bdh = float ( Ebdh.get () )
                hei = float ( Ehei.get () )

                lsa_b = (2*bdh*hei)+(2*lgh*bdh)

                Lans = gfx.Label ( cuboidlsa_b, text = str( str(lsa_b)+' is the lsa_b'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column = 1, row = 8 )

            Dbut = gfx.Button ( cuboidlsa_b, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 9)

        Bvol = gfx.Button ( cuboidhome, command = vol, text = 'Volume from dimensions',\
            fg = '#C0FF02', bg = '#222222',\
            bd = 2, relief = 'raised' )
        Bvol.grid ( column = 1, row = 1)

        Bcsa = gfx.Button ( cuboidhome, text = 'Find CSA', command = csa,\
            bg = '#222222', fg = '#C0FF02',\
            bd = 2, relief = 'raised' )
        Bcsa.grid ( column = 1, row = 2 )

        Blsa_l = gfx.Button ( cuboidhome, text = 'Find LSA along length', command = lsa_l,\
            bg = '#222222', fg = '#C0FF02',\
            bd = 2, relief = 'raised' )
        Blsa_l.grid ( column = 1, row = 3 )

        Blsa_b = gfx.Button ( cuboidhome, text = 'Find LSA along breadth', command = lsa_b,\
            bg = '#222222', fg = '#C0FF02',\
            bd = 2, relief = 'raised' )
        Blsa_b.grid ( column = 1, row = 4 )

    def sphere () :
        spherehome = gfx.Tk ()
        spherehome.configure(bg = '#222222')
        spherehome.title ('Sphere options')

        def vol () :
            spherevol = gfx.Tk ()
            spherevol.configure( bg = '#222222', bd = 5, relief='sunken' )
            spherevol.title('spherevol')

            Lrad = gfx.Label ( spherevol, text = 'ENter the radius',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised')
            Lrad.grid ( column = 1, row = 1 )

            Erad = gfx.Entry ( spherevol,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Erad.grid ( column = 1, row = 2)

            def Done () :
                rad = float ( Erad.get () )

                vol = (4/3)*(22/7)*(rad**3)

                Lans = gfx.Label ( spherevol, text = str(str(vol) + ' is the volume'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column=1, row = 4 )

            Dbut = gfx.Button ( spherevol, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd= 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 3)
        
        def csa () :
            spherecsa = gfx.Tk ()
            spherecsa.configure( bg = '#222222', bd = 5, relief='sunken' )
            spherecsa.title('spherecsa')

            Lrad = gfx.Label ( spherecsa, text = 'ENter the radius',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised')
            Lrad.grid ( column = 1, row = 1 )

            Erad = gfx.Entry ( spherecsa,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Erad.grid ( column = 1, row = 2)

            def Done () :
                rad = float ( Erad.get () )

                csa = 4*(22/7)*(rad**2)

                Lans = gfx.Label ( spherecsa, text = str(str(csa) + ' is the csa'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column=1, row = 4 )

            Dbut = gfx.Button ( spherecsa, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd= 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 3)


        Bvol = gfx.Button ( spherehome, command = vol, text = 'Find volume',\
            bg = '#C0FF02', fg = '#222222',\
            bd = 2, relief = 'raised' )
        Bvol.grid ( column = 1, row = 1 )

        Bcsa = gfx.Button ( spherehome, command = csa, text = 'Find csa',\
            bg = '#C0FF02', fg = '#222222',\
            bd = 2, relief = 'raised' )
        Bcsa.grid ( column = 1, row = 2 )

    def cylinder () :
        cylinderhome = gfx.Tk ()
        cylinderhome.configure(bg = '#222222')
        cylinderhome.title ('cylinder options')

        def vol () :
            cylindervol = gfx.Tk ()
            cylindervol.configure( bg = '#222222', bd = 5, relief='sunken' )
            cylindervol.title('cylindervol')

            Lrad = gfx.Label ( cylindervol, text = 'ENter the radius',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised')
            Lrad.grid ( column = 1, row = 1 )

            Erad = gfx.Entry ( cylindervol,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Erad.grid ( column = 1, row = 2)

            Lhei = gfx.Label ( cylindervol, text = 'Enter the height',\
                    bg = '#222222', fg = '#C0FF02',\
                    bd = 2, relief = 'raised' )
            Lhei.grid ( column = 1, row = 3 )

            Ehei = gfx.Entry ( cylindervol,\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row = 4)


            def Done () :
                rad = float ( Erad.get () )
                hei = float ( Ehei.get () )

                vol = (22/7)*(rad**2)*hei

                Lans = gfx.Label ( cylindervol, text = str(str(vol) + ' is the volume'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column=1, row = 6 )

            Dbut = gfx.Button ( cylindervol, command = Done, text = 'Done',\
                    bg = '#C0FF02', fg = '#222222',\
                bd= 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 5)
        
        def csa () :
            cylindercsa = gfx.Tk ()
            cylindercsa.configure( bg = '#222222', bd = 5, relief='sunken' )
            cylindercsa.title('cylindercsa')

            Lrad = gfx.Label ( cylindercsa, text = 'ENter the radius',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised')
            
            Lrad.grid ( column = 1, row = 1 )

            Erad = gfx.Entry ( cylindercsa,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Erad.grid ( column = 1, row = 2)

            Lhei = gfx.Label ( cylindercsa, text = 'Enter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column = 1, row = 3 )

            Ehei = gfx.Entry ( cylindercsa,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row = 4)

            def Done () :
                rad = float ( Erad.get () )
                hei = float ( Ehei.get () )

                csa = (2*(22/7)*rad*hei) + (2*(22/7)*rad*rad)

                Lans = gfx.Label ( cylindercsa, text = str(str(csa) + ' is the csa'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column=1, row = 6 )

            Dbut = gfx.Button ( cylindercsa, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd= 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 5)

        def lsa () :
            cylinderlsa = gfx.Tk ()
            cylinderlsa.configure( bg = '#222222', bd = 5, relief='sunken' )
            cylinderlsa.title('cylinderlsa')

            Lrad = gfx.Label ( cylinderlsa, text = 'ENter the radius',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised')
            
            Lrad.grid ( column = 1, row = 1 )

            Erad = gfx.Entry ( cylinderlsa,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Erad.grid ( column = 1, row = 2)

            Lhei = gfx.Label ( cylinderlsa, text = 'Enter the height',\
                bg = '#222222', fg = '#C0FF02',\
                bd = 2, relief = 'raised' )
            Lhei.grid ( column = 1, row = 3 )

            Ehei = gfx.Entry ( cylinderlsa,\
                bg = '#C0FF02', fg = '#222222',\
                bd = 2, relief = 'sunken' )
            Ehei.grid ( column = 1, row = 4)

            def Done () :
                rad = float ( Erad.get () )
                hei = float ( Ehei.get () )

                lsa = 2*(22/7)*rad*hei

                Lans = gfx.Label ( cylinderlsa, text = str(str(lsa) + ' is the lsa'),\
                    bg = '#C0FF02', fg = '#222222',\
                    bd = 2, relief = 'raised' )
                Lans.grid ( column=1, row = 6 )

            Dbut = gfx.Button ( cylinderlsa, command = Done, text = 'Done',\
                bg = '#C0FF02', fg = '#222222',\
                bd= 2, relief = 'raised' )
            Dbut.grid ( column = 1, row = 5)

        Bvol = gfx.Button ( cylinderhome, command = vol, text = 'Find volume',\
            bg = '#C0FF02', fg = '#222222',\
            bd = 2, relief = 'raised' )
        Bvol.grid ( column = 1, row = 1 )

        Blsa = gfx.Button ( cylinderhome, command = lsa, text = 'Find lsa',\
            bg = '#C0FF02', fg = '#222222',\
            bd = 2, relief = 'raised' )
        Blsa.grid ( column = 1, row = 2 )

        Bcsa = gfx.Button ( cylinderhome, command = csa, text = 'Find csa',\
            bg = '#C0FF02', fg = '#222222',\
            bd = 2, relief = 'raised' )
        Bcsa.grid ( column = 1, row = 3 )
    #%% Buttons

    Bcube = gfx.Button ( mensurator3dhome, command = cube, text = 'Cube',\
                        bg = '#222222', fg = '#C0FF02',\
                        bd = 2, relief = 'raised' )
    Bcube.grid (column = 1, row = 2)

    Bcuboid = gfx.Button ( mensurator3dhome, command = cuboid, text = 'Cuboid',\
                        bg = '#222222', fg = '#C0FF02',\
                        bd = 2, relief = 'raised' )
    Bcuboid.grid (column = 1, row = 3)

    Bsphere = gfx.Button ( mensurator3dhome, command = sphere, text = 'Sphere',\
        bg = '#222222', fg = '#C0FF02',\
        bd = 2, relief = 'raised' )
    Bsphere.grid ( column = 1, row = 4 )

    Bcylinder = gfx.Button ( mensurator3dhome, command = cylinder, text = 'cylinder',\
        bg = '#222222', fg = '#C0FF02',\
        bd = 2, relief = 'raised' )
    Bcylinder.grid ( column = 1, row = 5 )

    #%% mainloops

    mensurator3dhome.mainloop ()

mensurator3d()