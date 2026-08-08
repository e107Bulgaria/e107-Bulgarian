<?php

if (!defined('e107_INIT')) { exit; }

// Примерен конфигурационен файл на тема.
class theme__blank implements e_theme_config
{
	function process()
	{
		$pref = e107::getConfig();
		$tp = e107::getParser();

		$theme_pref = array();
		$theme_pref['example'] = $tp->toDb($_POST['_blank_example']);
		$theme_pref['example2'] = $tp->toDb($_POST['_blank_example2']);

		$pref->set('sitetheme_pref', $theme_pref);
		return $pref->dataHasChanged();
	}

	function config()
	{
		$frm = e107::getForm();

		$var[0]['caption'] = "Примерно конфигурационно поле";
		$var[0]['html'] = $frm->text('_blank_example', e107::pref('theme', 'example', 'default'));
		$var[0]['help'] = "Примерен помощен текст за това поле.";

		$var[1]['caption'] = "Примерно конфигурационно поле 2";
		$var[1]['html'] = $frm->text('_blank_example2', e107::pref('theme', 'example2', 'default'));

		return $var;
	}

	function help()
	{
		return "
			<div class='well'>
				<a href='https://e107.org'>Примерно HTML съдържание за помощната секция</a>.<br /><br />
				Този конфигурационен файл е пример за разработчици на e107 теми. Използвайте го като отправна точка за собствени настройки на темата.
				<ul>
					<li>Добавяне на конфигурационни полета</li>
					<li>Записване на стойности</li>
					<li>Помощни описания към настройките</li>
					<li>Персонализиране на темата</li>
				</ul>
			</div>
		";
	}
}

?>