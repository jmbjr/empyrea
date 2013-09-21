import libtcodpy as libtcod
	
libtcod.console_set_custom_font('fonts\\dullard14x14.png',libtcod.FONT_LAYOUT_TCOD,32,32)

libtcod.console_init_root(80,50,'test',False)
testconsole = libtcod.console_new(80,50)
libtcod.console_map_ascii_code_to_font(157,4,5) # Deciduous
libtcod.console_map_ascii_code_to_font(156,1,5) # Shrubland
libtcod.console_map_ascii_code_to_font(154,2,5) # Cacti
libtcod.console_map_ascii_code_to_font(153,3,5) # Heathland
libtcod.console_map_ascii_code_to_font(151,0,5) # Broadleaf
libtcod.console_map_ascii_code_to_font(150,5,5) # Mixed Forest
libtcod.console_map_ascii_code_to_font(149,0,2) # Coniferous
libtcod.console_map_ascii_code_to_font(148,6,5) # Evergreen
libtcod.console_map_ascii_code_to_font(147,7,5) # Caves
libtcod.console_map_ascii_code_to_font(146,8,5) # Tropical Forest 
key=libtcod.Key()
mouse=libtcod.Mouse() 
while not libtcod.console_is_window_closed():
    libtcod.console_clear(None)

    libtcod.console_print_ex(testconsole,10,40,libtcod.BKGND_NONE,libtcod.LEFT,'@')
    libtcod.console_print_ex(testconsole,11,40,libtcod.BKGND_NONE,libtcod.LEFT,chr(146))
    libtcod.console_put_char(testconsole,12,40,147)
    libtcod.console_put_char(testconsole,13,40,148)
    libtcod.console_put_char(testconsole,14,40,149)
    libtcod.console_put_char(testconsole,15,40,150)
    libtcod.console_put_char(testconsole,16,40,151)
    libtcod.console_put_char(testconsole,17,40,153)
    libtcod.console_put_char(testconsole,18,40,154)
    libtcod.console_put_char(testconsole,19,40,156)
    libtcod.console_print_ex(testconsole,20,40,libtcod.BKGND_NONE,libtcod.LEFT,'C')
    libtcod.console_blit(testconsole,0,0,80,50,0,0,0)
    libtcod.console_flush()
    libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS,key,mouse,True)
