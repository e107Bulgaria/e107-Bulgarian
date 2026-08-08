<?php
/*
 * e107 website system
 * Bootstrap3 page template - Bulgarian localized overlay.
 */
if (!defined('e107_INIT')) { exit; }

$PAGE_WRAPPER = array();
$PAGE_TEMPLATE = array();

global $sc_style;

$sc_style['CPAGEAUTHOR|default']['pre'] = '';
$sc_style['CPAGEAUTHOR|default']['post'] = ", ";
$sc_style['CPAGESUBTITLE|default']['pre'] = '<h2>';
$sc_style['CPAGESUBTITLE|default']['post'] = '</h2>';
$sc_style['CPAGEMESSAGE|default']['pre'] = '';
$sc_style['CPAGEMESSAGE|default']['post'] = '<div class="clear"><!-- --></div>';
$sc_style['CPAGENAV|default']['pre'] = '<div class="f-right pull-right col-md-3">';
$sc_style['CPAGENAV|default']['post'] = '</div>';

$PAGE_TEMPLATE['default']['page'] = '
	{PAGE}
	{PAGECOMMENTS}
';
$PAGE_TEMPLATE['default']['start'] = '<div id="{CPAGESEF}" class="cpage_body cpage-body">{CHAPTER_BREADCRUMB}';
$PAGE_TEMPLATE['default']['body'] = '
	{CPAGEMESSAGE|default}
	{CPAGESUBTITLE|default}
	<div class="clear"><!-- --></div>
	{CPAGENAV|default}
	{CPAGEBODY|default}
	<div class="clear"><!-- --></div>
	{CPAGERATING|default}
	{CPAGEEDIT}
';
$PAGE_WRAPPER['default']['CPAGEEDIT'] = "<div class='text-right'>{---}</div>";

$PAGE_TEMPLATE['default']['authorize'] = '
	<div class="cpage-restrict ">
		{message}
		{form_open}
		<div class="panel panel-default">
			<div class="panel-heading">{caption}</div>
			<div class="panel-body">
			    <div class="form-group">
			       <label class="col-sm-3 control-label">{label}</label>
			       <div class="col-sm-9">{password} {submit}</div>
			    </div>
			</div>
		</div>
		{form_close}
	</div>
';
$PAGE_TEMPLATE['default']['restricted'] = '{text}';
$PAGE_TEMPLATE['default']['notfound'] = '{text}';
$PAGE_TEMPLATE['default']['end'] = '{CPAGERELATED: types=page,news}</div>';
$PAGE_TEMPLATE['default']['tableRender'] = 'cpage';

$PAGE_TEMPLATE['default']['related']['start'] = '{SETIMAGE: w=350&h=350&crop=1}<h2 class="caption">{LAN=LAN_RELATED}</h2><div class="row">';
$PAGE_TEMPLATE['default']['related']['item'] = '<div class="col-md-4"><a href="{RELATED_URL}">{RELATED_IMAGE}</a><h3><a href="{RELATED_URL}">{RELATED_TITLE}</a></h3></div>';
$PAGE_TEMPLATE['default']['related']['end'] = '</div>';

$PAGE_TEMPLATE['custom']['start'] = '<div id="{CPAGESEF}" class="cpage-body">';
$PAGE_TEMPLATE['custom']['body'] = '';
$PAGE_TEMPLATE['custom']['authorize'] = '';
$PAGE_TEMPLATE['custom']['restricted'] = '';
$PAGE_TEMPLATE['custom']['end'] = '</div>';
$PAGE_TEMPLATE['custom']['tableRender'] = '';

$PAGE_WRAPPER['profile']['CMENUIMAGE: template=profile'] = '<span class="page-profile-image pull-left col-xs-12 col-sm-4 col-md-4">{---}</span>';
$PAGE_TEMPLATE['profile'] = $PAGE_TEMPLATE['default'];
$PAGE_TEMPLATE['profile']['body'] = '
	{CPAGEMESSAGE}
	{CPAGESUBTITLE}
	<div class="clear"><!-- --></div>
	{CPAGENAV|default}
	{SETIMAGE: w=320}
	{CMENUIMAGE: template=profile}
	{CPAGEBODY}
	<div class="clear"><!-- --></div>
	{CPAGERATING}
	{CPAGEEDIT}
';

$PAGE_TEMPLATE['customfields'] = $PAGE_TEMPLATE['default'];
$PAGE_WRAPPER['customfields']['CPAGEFIELDTITLE'] = "<tr id='customfields-{CPAGEFIELDNAME}'><td>{---}</td>";
$PAGE_WRAPPER['customfields']['CPAGEFIELD'] = "<td>{---}</td></tr>";
$PAGE_WRAPPER['customfields']['CPAGEFIELD: name=myvideo'] = "<tr><td colspan='2'>{---}</td></tr>";
$PAGE_WRAPPER['customfields']['CPAGEFIELD: name=myimage'] = "<td><a class='e-modal' data-modal-caption='{CPAGEFIELDTITLE: name=myimage}' target='_blank' href='{CPAGEFIELD: name=myimage&mode=raw&w=800}'>{---}</a></td></tr>";
$PAGE_WRAPPER['customfields']['CPAGEFIELD: name=myurl&mode=raw'] = "<td><a class='btn btn-primary' target='_blank' href='{---}'>Преглед на уебсайта</a></td></tr>";

$PAGE_TEMPLATE['customfields']['body'] = '
	<div id="custom-fields-example" class="col-xs-12 col-md-5 pull-right" style="margin-right:-15px">
	<table class="table table-striped table-bordered">
		<tr><th class="text-center" colspan="2">Допълнителни полета</th></tr>
		{CPAGEFIELD: name=myvideo}
		{CPAGEFIELDTITLE: name=mybbarea}{CPAGEFIELD: name=mybbarea}
		{CPAGEFIELDTITLE: name=myboolean}{CPAGEFIELD: name=myboolean}
		{CPAGEFIELDTITLE: name=mycheckbox}{CPAGEFIELD: name=mycheckbox}
		{CPAGEFIELDTITLE: name=mycountry}{CPAGEFIELD: name=mycountry}
		{CPAGEFIELDTITLE: name=mydatestamp}{CPAGEFIELD: name=mydatestamp}
		{CPAGEFIELDTITLE: name=mydropdown}{CPAGEFIELD: name=mydropdown}
		{CPAGEFIELDTITLE: name=myemail}{CPAGEFIELD: name=myemail&mode=raw}
		{CPAGEFIELDTITLE: name=myemail}{CPAGEFIELD: name=myemail}
		{CPAGEFIELDTITLE: name=myfile}{CPAGEFIELD: name=myfile}
		{CPAGEFIELDTITLE: name=myicon}{CPAGEFIELD: name=myicon}
		{SETIMAGE: w=200}
		{CPAGEFIELDTITLE: name=myimage}{CPAGEFIELD: name=myimage}
		{CPAGEFIELDTITLE: name=mylanguage}{CPAGEFIELD: name=mylanguage}
		{CPAGEFIELDTITLE: name=mynumber}{CPAGEFIELD: name=mynumber}
		{CPAGEFIELDTITLE: name=myprogressbar}{CPAGEFIELD: name=myprogressbar}
		{CPAGEFIELDTITLE: name=mytags}{CPAGEFIELD: name=mytags}
		{CPAGEFIELDTITLE: name=mytext}{CPAGEFIELD: name=mytext}
		{CPAGEFIELDTITLE: name=myurl}{CPAGEFIELD: name=myurl}
		{CPAGEFIELDTITLE: name=myurl}{CPAGEFIELD: name=myurl&mode=raw}
	</table>
	{CPAGEEDIT}
	</div>
	{CPAGEBODY}
	{CPAGEMESSAGE}
	{CPAGESUBTITLE}
	<div class="clear"><!-- --></div>
	{CPAGEFIELDS_DISABLED: generate}
	{CPAGEFIELDS_DISABLED}
	{CPAGENAV}
	<div class="clear"><!-- --></div>
	{CPAGERATING}
';
