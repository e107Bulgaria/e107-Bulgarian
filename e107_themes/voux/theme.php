<?php
/**
 * Voux Blog Theme for e107 v2.x - Bulgarian localized overlay.
 */
if (!defined('e107_INIT')) { exit; }

define("BOOTSTRAP", 3);
define("FONTAWESOME", 4);
define('VIEWPORT', "width=device-width, initial-scale=1.0");

e107::library('load', 'bootstrap');
e107::library('load', 'fontawesome');

e107::css('url', 'https://fonts.googleapis.com/css?family=Bad+Script|Raleway:400,500,600,700,300|Lora:400');
e107::css('url', 'https://fonts.googleapis.com/css?family=Montserrat:400,700&ver=4.2.4');
e107::css('url', 'https://fonts.googleapis.com/css?family=Domine:400,700&ver=4.2.4');
e107::css('url', 'https://fonts.googleapis.com/css?family=Lato:300,400,700,400italic&ver=4.2.4');
e107::css('url', 'https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,700italic,400,700,300&subset=latin,cyrillic-ext&ver=3.9.2');

define('OTHERNEWS_COLS',false);
define('OTHERNEWS_LIMIT', 3);
define('OTHERNEWS2_COLS',false);
define('OTHERNEWS2_LIMIT', 3);
define('COMMENTLINK', 'Коментари ');
define('COMMENTOFFSTRING', 'Коментарите са изключени');
define('PRE_EXTENDEDSTRING', '<br />');

function tablestyle($caption, $text, $id='', $info=array())
{
	$style = $info['setStyle'];
	$type = $style;

	if(empty($caption))
	{
		$type = 'box';
	}

	if($style == 'navdoc' || $style == 'none')
	{
		echo $text;
		return;
	}

	if($style == 'jumbotron')
	{
		echo '<div class="jumbotron"><div class="container">';
		if(!empty($caption))
		{
			echo '<h1>'.$caption.'</h1>';
		}
		echo $text.'</div></div>';
		return;
	}

	if($style == 'col-md-3' || $style == 'col-md-4' || $style == 'col-md-6' || $style == 'col-md-8' || $style == 'col-md-9')
	{
		echo '<div class="col-xs-12 '.$style.'">';
		if(!empty($caption))
		{
			echo '<h2>'.$caption.'</h2>';
		}
		echo $text.'</div>';
		return;
	}

	if($style == 'menu')
	{
		echo '<div class="menu"><h2 class="title">'.$caption.'</h2><div class="content">'.$text.'</div></div>';
		return;
	}

	if($style == 'portfolio')
	{
		echo '<div class="col-lg-4 col-md-4 col-sm-6">'.$text.'</div>';
		return;
	}

	if(!empty($caption))
	{
		echo '<h2 class="caption">'.$caption.'</h2>';
	}
	echo $text;
}

$LAYOUT['_header_'] = '
<div class="navbar navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Превключване на навигацията</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>
        <div class="navbar-collapse collapse {BOOTSTRAP_NAV_ALIGN}">
        	{NAVIGATION=main}
         	{BOOTSTRAP_USERNAV: placement=top}
         	<div class="nav navbar-nav navbar-right">{XURL_ICONS: size=2x&tip=0}</div>
        </div>
      </div>
    </div>
	<div class="container">
		<div id="logo"><h1><a href="{SITEURL}">{SITELOGO: w=300}</a></h1></div>
	</div>
';

$LAYOUT['_footer_'] = '
</div>
<div class="container">
   <div class="row">
      {SETSTYLE=menu}
		<div class="col-lg-4">{MENU=100}</div>
		<div class="col-lg-4">{MENU=101}</div>
		<div class="col-lg-4">{MENU=102}</div>
	</div>
</div>
{SETSTYLE=default}
<footer>
	<div class="container">
		<div class="row">
			<div>
				<div class="col-lg-6">{MENU=110}</div>
				<div class="col-lg-6">{MENU=111}</div>
			</div>
			<div>
				<div class="col-sm-12 col-lg-4">{MENU=112}</div>
				<div class="col-sm-12 col-lg-8">{MENU=113}</div>
			</div>
		</div>
	</div>
	<div class="container"><div class="row"><div class="col-lg-12">{MENU=114}</div></div></div>
	<div class="container">
		<div class="row"><div class="col-lg-12">{MENU=115}{NAVIGATION=footer}{MENU=116}</div></div>
	</div>

	<div class="subscribe-box">
	  <div class="container">
	    <div class="block">
		  <div class="row">
      		<div class="col-lg-offset-1 col-lg-5 col-sm-6">
		         <div class="caption">
		            <img class="img-responsive" src="'.THEME_ABS.'install/sketch-subscribe.png" alt="Изображение за абонамент" />
		         </div>
            </div>
            <div class="col-lg-6 col-sm-6">{VOUX_NEWSLETTER_FORM}</div>
          </div>
        </div>
      </div>
    </div>

	<div id="footer-social">
		<div class="container"><div class="row"><div class="col-lg-12 text-center footer-xurl">{XURL_ICONS: size=2x&tip=0}</div></div></div>
	</div>

	<div id="footer-copyright" class="container">
		<div class="row">
			<div class="col-lg-8">
				<small>{SITEDISCLAIMER}</small><br />
				<small>e107 тема, базирана на &quot;Voux&quot; от <a href="https://www.themexpose.com/">ThemeXpose</a>, разпространявана съгласно условията на GNU General Public License.</small>
			</div>
			<div class="col-lg-4">{BOOTSTRAP_USERNAV: placement=bottom&dir=up}</div>
		</div>
	</div>
</footer>
';

$LAYOUT['jumbotron_home'] = <<<TMPL
  <div class="container">{ALERTS}</div>
    {SETSTYLE=jumbotron}
	{WMESSAGE=force}
	{SETSTYLE=default}
	<div class="container">
	{MENU=1}
	{---}
	</div>
    <div class="container">
      <div class="row">
      {SETSTYLE=col-md-4}
	  {MENU=2}{MENU=3}{MENU=4}
      </div>
      <div class="row">
      {SETSTYLE=col-md-4}
	  {MENU=5}{MENU=6}{MENU=7}
      </div>
      {SETSTYLE=default}
      <div class="row">
		<div class="col-lg-6">{MENU=8}</div>
		<div class="col-lg-6">{MENU=9}</div>
		<div class="col-sm-12 col-lg-4">{MENU=10}</div>
		<div class="col-sm-12 col-lg-8">{MENU=11}</div>
		<div class="col-sm-12 col-lg-8">{MENU=12}</div>
		<div class="col-sm-12 col-lg-4">{MENU=13}</div>
		<div class="col-lg-12">{MENU=14}</div>
	  </div>
TMPL;

$LAYOUT['modern_business_home'] = <<<TMPL
    {SETSTYLE=none}
	{FEATUREBOX}
	<div class="container">{ALERTS}{MENU=1}</div>
	<div class="section">
	    <div class="container">
	      <div class="row">
	      {SETSTYLE=col-md-4}
		  {CMENU=jumbotron-menu-1}
		  {CMENU=jumbotron-menu-2}
		  {CMENU=jumbotron-menu-3}
	      </div>
		</div>
	</div>
	{SETSTYLE=default}
	<div class="section-colored text-center">
      <div class="container"><div class="row"><div class="col-lg-12">{WMESSAGE}<hr></div></div></div>
 	</div>
	<div class="section">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 text-center">
            <h2>Покажете част от работата си в портфолиото на началната страница</h2>
            <hr>
          </div>
		  {SETSTYLE=portfolio}
		  {SETIMAGE: w=700&h=500&crop=1}
		  {GALLERY_PORTFOLIO: placeholder=1&limit=6}
        </div>
      </div>
    </div>
	{SETSTYLE=none}
	<div class="section-colored"><div class="container"><div class="row">{CMENU=feature-menu-1}</div></div></div>
	<div class="section"><div class="container"><div class="row">{CMENU=feature-menu-2}</div></div></div>
	<div class="container"><div class="row well">{CMENU=feature-menu-3}</div></div>
	<div class="container">
	{---}
TMPL;

$LAYOUT['jumbotron_full'] = '
	{SETSTYLE=default}
	<div class="container">
	{ALERTS}
	{MENU=1}
	{---}
	</div>
    <div class="container">
';

$LAYOUT['jumbotron_sidebar_right'] = '
	{SETSTYLE=default}
	<div class="container">
	{ALERTS}
		<div class="row">
   			<div class="col-xs-12 col-md-8">{---}</div>
        	<div id="sidebar" class="col-xs-12 col-md-4">
        	{SETSTYLE=menu}
        	{SETIMAGE: w=400}
        		{MENU=1}
        	</div>
      	</div>
	</div>
    <div class="container">
       {SETSTYLE=default}
       <div class="row">
			<div class="col-lg-6">{MENU=2}</div>
			<div class="col-lg-6">{MENU=3}</div>
			<div class="col-sm-12 col-lg-4">{MENU=4}</div>
			<div class="col-sm-12 col-lg-8">{MENU=5}</div>
			<div class="col-sm-12 col-lg-8">{MENU=6}</div>
			<div class="col-sm-12 col-lg-4">{MENU=7}</div>
			<div class="col-lg-12">{MENU=8}</div>
	   </div>
	</div>
    <div class="container">
';

?>
