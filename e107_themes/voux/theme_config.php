<?php

if (!defined('e107_INIT')) { exit; }

class theme_config implements e_theme_config
{
	function config()
	{
		$brandingOpts = array(
			'sitename'=>'Име на сайта',
			'logo' => 'Лого',
			'sitenamelogo'=>'Лого &amp; име на сайта'
		);

		$fields = array(
			'branding'          => array('title'=> "Брандиране", 'type'=>'dropdown', 'writeParms'=>array('optArray'=> $brandingOpts)),
			'nav_alignment'     => array('title'=> "Подравняване на навигационната лента", 'type'=>'dropdown', 'writeParms'=>array('optArray'=> array('left'=> "Вляво",'right'=> "Вдясно"))),
			'usernav_placement' => array('title'=> "Позиция на регистрация/вход", 'type'=>'dropdown', 'writeParms'=>array('optArray'=> array('top'=> "Отгоре", 'bottom'=> "Отдолу"))),
		);

		return $fields;
	}

	function help()
	{
		return '';
	}
}

?>