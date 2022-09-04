<?php
/**
 * Website Builder Theme functions and definitions
 *
 * @link https://developer.wordpress.org/themes/basics/theme-functions/
 *
 * @package Website Builder Theme
 */


















use Wb4WpTheme\Managers\Blog_Manager;
use Wb4WpTheme\Managers\Customize_Manager;
use Wb4WpTheme\Managers\Template_Manager;
use Wb4WpTheme\Managers\Update_Manager;

if ( ! defined( '_WEBSITE_BUILDER_THEME_VERSION' ) ) {
	// Replace the version number of the theme on each release.
	define( '_WEBSITE_BUILDER_THEME_VERSION', '1.0.0' );
}

if ( ! defined( 'WB4WP_THEME_VERSION' ) ) {
	define( 'WB4WP_THEME_VERSION', wp_get_theme()->Version );
}

// Load all the required files.
if ( file_exists( __DIR__ . '/vendor/autoload.php' ) ) {
	require_once __DIR__ . '/vendor/autoload.php';
}

define( 'WB4WP_PROVIDER_NAME', 'Website Builder' );
define( 'WB4WP_UPDATE_URL', 'https://wp-versions.builderservices.io/content/theme-version.json' );

add_action( 'after_setup_theme', 'wb4wp_theme_setup' );

if ( ! function_exists( 'wb4wp_theme_setup' ) ) :

	/**
	 * Setup WB4WP theme.
	 */
	function wb4wp_theme_setup() {
		add_theme_support( 'title-tag' );
		add_theme_support( 'post-thumbnails' );
		add_theme_support( 'woocommerce' );
		add_theme_support( 'responsive-embeds' );

		// This theme uses wp_nav_menu() in one location.
		register_nav_menus(
			array(
				'wb4wp' => esc_html__( 'Primary', 'wb4wp_theme' ),
			)
		);

		/*
		 * Switch default core markup for search form, comment form, and comments
		 * to output valid HTML5.
		 */
		add_theme_support(
			'html5',
			array(
				'search-form',
				'comment-form',
				'comment-list',
				'gallery',
				'caption',
				'style',
				'script',
			)
		);
	}
endif;

if ( ! function_exists( 'storefront_is_woocommerce_activated' ) ) {
	/**
	 * Query WooCommerce activation
	 */
	function storefront_is_woocommerce_activated() {
		return class_exists( 'WooCommerce' );
	}
}

if ( ! function_exists( 'jetpack_is_installed_and_activated' ) ) {
	/**
	 * Query Jetpack activation
	 *
	 * @return bool
	 */
	function jetpack_is_installed_and_activated() {
		return class_exists( 'Jetpack' );
	}
}

if ( storefront_is_woocommerce_activated() ) {
	require __DIR__ . '/src/woocommerce/single-product-summary.php';
	require __DIR__ . '/src/woocommerce/shop-loop.php';
	require __DIR__ . '/src/woocommerce/cart-page.php';
	require __DIR__ . '/src/woocommerce/checkout-page.php';
}

/**
 * Enqueue theme style assets.
 */
function wb4wp_theme_enqueue_style() {
	$theme_name = 'wb4wp-theme';
	wp_enqueue_style( $theme_name, get_template_directory_uri() . '/dist/main.css', false, WB4WP_THEME_VERSION );

	if ( have_posts() ) {
		wp_enqueue_style( $theme_name . '-blog', get_template_directory_uri() . '/dist/blog/blog.css', false, WB4WP_THEME_VERSION );
	}

	if ( storefront_is_woocommerce_activated() ) {
		wp_enqueue_script(
			$theme_name . '-woocommerce-js',
			get_template_directory_uri() . '/dist/woocommerce/woocommerce.js',
			array(),
			WB4WP_THEME_VERSION,
			true
		);
		wp_enqueue_style( $theme_name . '-woocommerce', get_template_directory_uri() . '/dist/woocommerce/woocommerce.css', false, WB4WP_THEME_VERSION );
	}

	if ( jetpack_is_installed_and_activated() ) {
		wp_enqueue_style( $theme_name . '-jetpack', get_template_directory_uri() . '/dist/jetpack/jetpack.css', false, WB4WP_THEME_VERSION );
	}

	$template_manager = new Template_Manager();
	$template_manager->render_template_assets( $theme_name );
}

add_action( 'wp_enqueue_scripts', 'wb4wp_theme_enqueue_style' );

/**
 * Initialize the wb4wp customize controls.
 *
 * @param WP_Customize_Manager $wp_customize .
 */
function wb4wp_theme_customizer( $wp_customize ) {
	$customize_manager = new Customize_Manager( $wp_customize );
	$customize_manager->register_controls();

	wp_enqueue_style( 'wb4wp-theme_customize-style', get_template_directory_uri() . '/dist/customize.css', false, WB4WP_THEME_VERSION );
}

add_action( 'customize_register', 'wb4wp_theme_customizer' );

/**
 * Enqueue a script to fix customize checkboxes.
 */
function wb4wp_customize_checkbox_fix() {
	wp_enqueue_script(
		'wb4wp_customize_checkbox_fix',
		get_template_directory_uri() . '/src/customizer/customize-checkbox-fix.js',
		array( 'jquery', 'customize-controls' ),
		WB4WP_THEME_VERSION,
		true
	);
}

add_action( 'customize_controls_enqueue_scripts', 'wb4wp_customize_checkbox_fix' );

/**
 * Enqueue a script to handle customize preview page changes.
 */
function wb4wp_customize_preview_page() {
	$script_handle = 'wb4wp_customize_preview_page';

	wp_enqueue_script(
		$script_handle,
		get_template_directory_uri() . '/src/customizer/customize-preview-page.js',
		array( 'jquery', 'customize-controls' ),
		WB4WP_THEME_VERSION,
		true
	);

	wp_localize_script(
		$script_handle,
		'wb4wpUrls',
		array(
			'base'         => get_site_url(),
			'singlePost'   => Blog_Manager::get_most_recent_post_url(),
			'blogOverview' => Blog_Manager::get_overview_url(),
		)
	);
}

add_action( 'customize_controls_enqueue_scripts', 'wb4wp_customize_preview_page' );

/**
 * Add menu pages.
 */
function wb4wp_add_menu_pages() {
	global $submenu;

	// phpcs:ignore WordPress.WP.GlobalVariablesOverride.Prohibited
	$submenu['themes.php'][500] = array(
		'Edit ' . WB4WP_PROVIDER_NAME . ' settings',
		'edit_theme_options',
		'admin.php?page=wb4wp-editor&wp-edit-link=/appearance',
	);
}

add_action( 'admin_menu', 'wb4wp_add_menu_pages' );

/**
 * Initialize wb4wp theme.
 */
function wb4wp_theme_init() {
	// This theme support page wide sections.
	add_theme_support( 'align-wide' );

	$update_manager = new Update_Manager();
	$update_manager->check_for_updates();
}

add_action( 'init', 'wb4wp_theme_init' );

/**
 * Enqueue customize JS.
 */
function wb4wp_theme_customizer_js() {
	wp_enqueue_script(
		'wb4wp-theme-customizer-js',
		get_template_directory_uri() . '/src/customizer/customizer.js',
		array( 'jquery' ),
		WB4WP_THEME_VERSION,
		true
	);

	wp_localize_script(
		'wb4wp-theme-customizer-js',
		'wb4wpL10n',
		array(
			// translators: %s = provider name.
			'title_text' => sprintf( __( 'Open %s', 'wb4wp_theme' ), WB4WP_PROVIDER_NAME ),
			'home_url'   => get_site_url(),
		)
	);
}

add_action( 'customize_controls_enqueue_scripts', 'wb4wp_theme_customizer_js' );

function wb4wp_add_to_cart_fragments( $fragments ) {
	global $woocommerce;
	$items      = $woocommerce->cart->get_cart();
	$item_count = 0;

	foreach ( $items as $item ) {
		$item_count += $item['quantity'];
	}

	$fragments['item_count'] = $item_count;

	return $fragments;
}

add_filter( 'woocommerce_add_to_cart_fragments', 'wb4wp_add_to_cart_fragments', 10, 3 );


function wpschool_text_shortcode() {
    return '
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:400,500,600,700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="static/css/style.css">
    <link rel="stylesheet" href="static/css/bootstrap.min.css">
    <title>Calculator</title>
</head>
<body>
<div class="container ">
   
    <div class="row">
        <div class="calculator-content-title">
		<br>
            <h4>Кредитный калькулятор</h4>
        </div>
        
      <div class="col-md">
        
       <div class="p-3 border bg-light"> <div class="calculator-content-body-left-inputs">
            <div class="">Сумма кредита в тенге</div>
            <div class="input">
                <input type="number" id="total-cost" value="0" class="input-number">
            </div>
            <div class="input">
                <input type="range" min="61260000" max="500000000" step="20000000"id="total-cost-range" value="61260000" class="input-range">
            </div>
       
            <div class="">Срок кредита в месяцах</div>
            <div class="input">
                <input type="number" id="credit-term" value="0"  class="input-number">
            </div>
            <div class="input">
                <input type="range" min="3" max="84"  step="1" id="credit-term-range" value="0" class="input-range">
            </div>
    </div> </div>
      </div>
      <div class="col-md">
        <div class="p-3 border bg-light"> 
            <div class="final-results-wrapper">
            <p class="h4 calculator-content-title ">Наше предложение</p>

            <div class="final-result-item">
                <div class="">Сумма кредита</div>
                <div class="value" id="amount-of-credit"><span>₸</span> 0</div>
            </div>
            <div class="final-result-item">
                <div class="">Процентная ставка</div>
                <div class="value" id="percent">0<span>%</span></div>
            </div>
            <div class="final-result-item">
                <div class="">Ежемесячный платеж</div>
                <div class="value" id="monthly-payment"><span>₸</span> 0</div>
            </div>
             <!-- Кнопка-триггер модального окна -->

        </div>
          <div class="d-grid gap-2 col-6 mx-auto">
            <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal">Оставить Заявку</button>
          </div>
      </div>
      
      
    </div>
  </div>





  
  <!-- Модальное окно -->
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Оставить заявку на кредит</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Закрыть"></button>
        </div>
        <div class="modal-body">
            <div class="container py-4">

                <!-- Bootstrap 5 starter form -->
                  <form id="contactForm"  action="send.php" method="post">
 
              
                  <!-- Name input -->
                  <div class="mb-3">
                    <select class="form-control" id="mySelect" name="select_urlico" onchange="check()"> 
                        <option value="Форма физ./юр лица" selected>Форма физ./юр лица</option>
                        <option value="ТОО" >ТОО</option>
                </select>
                  </div>
                  <div class="demo">
                    
                  </div>
                                    <div class="mb-3">
                  <input class="form-control" type="text" id="fname" name="company_name" placeholder="Наименование юр.лица">
                </div>
            
                <div class="mb-3">
                    <div class="input-wrapper">
                        <div class="title">Сумма кредита в тенге</div>
                        <div class="input">
                            <input type="number" id="total-cost-cf" value="0" name="loan_sum" class="input-number">  
                        </div>
                        
                        <div class="input">
                            <input type="range" min="61260000" max="500000000" step="20000000"id="total-cost-range-cf" value="20000000" class="input-range">
                        </div>
                    </div>
               </div>
            
               <div class="mb-3">
                <div class="input-wrapper">
                    <div class="title">Срок кредита в месяцах</div>
                    <div class="input">
                        <input type="number" id="credit-term-cf" value="0"  class="input-number" name = "times">
                    </div>
                    <div class="input">
                        <input type="range" min="3" max="84"  step="1" id="credit-term-range-cf" value="0" class="input-range">
                    </div>
                </div>
              </div>
            
              <div class="mb-3">
              <p>Предлагаемое залоговое обеспечение            </p>
              <select class="form-control"   name="select_zalog"> 
              <option value="Движемое имещество">Движимое имущество                  </option>
              <option value="Недвижемое имущество" selected>Недвижимое имущество</option>
                 
              </select>
            </div>
            
            <div class="mb-3">
            <select class="form-control"  name="select_target"> 
                <option value="На приобретение основных средств">На приобретение основных средств</option>
                <option value="Целевое назначение кредита" selected>Целевое назначение кредита</option>
                <option value="На пополнение оборотных средств">На пополнение оборотных средств</option>
            </select>
            </div>
            
            <div class="mb-3">
            <select  class="form-control"  name="select_address"> 
                <option value="Район регистрации юр лица" selected>Район регистрации юр лица</option>
                <option value="Бостандыкский">Бостандыкский</option>
                <option value="Медеуский">Медеуский</option>
                <option value="Алмалинский">Алмалинский</option>
                <option value="Ауэзовский">Ауэзовский</option>
                <option value="Алатауский">Алатауский</option>
                <option value="Наурызбайский">Наурызбайский</option>
                <option value="Жетысуйский">Жетысуйский</option>
                <option value="Турксибский">Турксибский</option>
              </select>  
            </div>
            
            <div class="mb-3">
            <input class="form-control"  type="number" id="fname" name="phone" placeholder="Телефон">
            </div>
            
              
            
                  <!-- Email address input -->
                  <div class="mb-3">
                    <input class="form-control" id="emailAddress" name ="email"  type="email" placeholder="Email Address" data-sb-validations="required, email" />
                  </div>
              
                
              
                  <!-- Form submit button -->
                  <div class="d-grid">
                    <button class="btn btn-primary btn-lg"   type="submit" name="submit" value="Submit">Отправить</button>
                  </div>
                </form>
              </div>
        </div>
       
      </div>
    </div>
  </div>
  
   <script src="static/js/bootstrap.bundle.min.js"></script>
   <script src="static/js/main.js"></script> 
</body>
</html>

  ';
}


add_action('wp_enqueue_scripts','add_styles');
add_action('wp_footer','add_scripts');

function add_styles() {
	wp_enqueue_style('style_bootstrap',get_template_directory_uri() . '/calculator/bootstrap.min.css');
	wp_enqueue_style('style_carts',get_template_directory_uri() . '/calculator/cal_style.css');
}
	

function add_scripts() {
	wp_enqueue_script('script',get_template_directory_uri() . '/calculator/bootstrap.bundle.min.js');
		wp_enqueue_script('scripts',get_template_directory_uri() . '/calculator/calc.js');

}

add_shortcode('textshortcode', 'wpschool_text_shortcode');
