<?php


$_config = array();

// ----------------------------  CONFIG DB  ----------------------------- //
$_config['db']['1']['dbhost'] = 'localhost';
$_config['db']['1']['dbuser'] = 'root';
$_config['db']['1']['dbpw'] = 'root';
$_config['db']['1']['dbcharset'] = 'utf8';
$_config['db']['1']['pconnect'] = '0';
$_config['db']['1']['dbname'] = 'ultrax';
$_config['db']['1']['tablepre'] = 'pre_';
$_config['db']['common']['slave_except_table'] = '';

// --------------------------  CONFIG MEMORY  --------------------------- //
$_config['memory']['prefix'] = 'g4wr2i_';
$_config['memory']['eaccelerator'] = 1;
$_config['memory']['apc'] = 1;
$_config['memory']['xcache'] = 1;
$_config['memory']['memcache']['server'] = '';
$_config['memory']['memcache']['port'] = 11211;
$_config['memory']['memcache']['pconnect'] = 1;
$_config['memory']['memcache']['timeout'] = 1;

// --------------------------  CONFIG SERVER  --------------------------- //
$_config['server']['id'] = 1;

// -------------------------  CONFIG DOWNLOAD  -------------------------- //
$_config['download']['readmod'] = 2;
$_config['download']['xsendfile']['type'] = '0';
$_config['download']['xsendfile']['dir'] = '/down/';

// ---------------------------  CONFIG CACHE  --------------------------- //
$_config['cache']['type'] = 'sql';

// --------------------------  CONFIG OUTPUT  --------------------------- //
$_config['output']['charset'] = 'utf-8';
$_config['output']['forceheader'] = 1;
$_config['output']['gzip'] = '0';
$_config['output']['tplrefresh'] = 1;
$_config['output']['language'] = 'zh_cn';
$_config['output']['staticurl'] = 'static/';
$_config['output']['ajaxvalidate'] = '0';
$_config['output']['iecompatible'] = '0';

// --------------------------  CONFIG COOKIE  --------------------------- //
$_config['cookie']['cookiepre'] = '3mwc_';
$_config['cookie']['cookiedomain'] = '';
$_config['cookie']['cookiepath'] = '/';

// -------------------------  CONFIG SECURITY  -------------------------- //
$_config['security']['authkey'] = 'cad3d25nj9Can4M0';
$_config['security']['urlxssdefend'] = 1;
$_config['security']['attackevasive'] = '0';
$_config['security']['querysafe']['status'] = 1;
$_config['security']['querysafe']['dfunction']['0'] = 'load_file';
$_config['security']['querysafe']['dfunction']['1'] = 'hex';
$_config['security']['querysafe']['dfunction']['2'] = 'substring';
$_config['security']['querysafe']['dfunction']['3'] = 'if';
$_config['security']['querysafe']['dfunction']['4'] = 'ord';
$_config['security']['querysafe']['dfunction']['5'] = 'char';
$_config['security']['querysafe']['daction']['0'] = 'intooutfile';
$_config['security']['querysafe']['daction']['1'] = 'intodumpfile';
$_config['security']['querysafe']['daction']['2'] = 'unionselect';
$_config['security']['querysafe']['daction']['3'] = '(select';
$_config['security']['querysafe']['daction']['4'] = 'unionall';
$_config['security']['querysafe']['daction']['5'] = 'uniondistinct';
$_config['security']['querysafe']['dnote']['0'] = '/*';
$_config['security']['querysafe']['dnote']['1'] = '*/';
$_config['security']['querysafe']['dnote']['2'] = '#';
$_config['security']['querysafe']['dnote']['3'] = '--';
$_config['security']['querysafe']['dnote']['4'] = '"';
$_config['security']['querysafe']['dlikehex'] = 1;
$_config['security']['querysafe']['afullnote'] = '0';

// --------------------------  CONFIG ADMINCP  -------------------------- //
// -------- Founders: $_config['admincp']['founder'] = '1,2,3'; --------- //
$_config['admincp']['founder'] = '1';
$_config['admincp']['forcesecques'] = '0';
$_config['admincp']['checkip'] = 1;
$_config['admincp']['runquery'] = 1;
$_config['admincp']['dbimport'] = 1;

// --------------------------  CONFIG REMOTE  --------------------------- //
$_config['remote']['on'] = '0';
$_config['remote']['dir'] = 'remote';
$_config['remote']['appkey'] = '62cf0b3c3e6a4c9468e7216839721d8e';
$_config['remote']['cron'] = '0';


// -------------------  THE END  -------------------- //

?>