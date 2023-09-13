package activities;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class Assertions {

    //WebDriver driver;
    //ChromeOptions options;



   @Test
   public void setUp() throws InterruptedException {
       /* System.setProperty("webdriver.chrome.driver", "C://Users//06318O744//Maven//chromedriver_win32//chromedriver.exe");
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        DesiredCapabilities cp = new DesiredCapabilities();
        cp.setCapability(ChromeOptions.CAPABILITY, options);
        options.merge(cp);
        driver = new ChromeDriver(options);
        driver.get("http://alchemy.hguy.co:8080/orangehrm/symfony/web/index.php/auth/login");
        Thread.sleep(3000);*/
        // System.setProperty(FirefoxDriver.SystemProperty.BROWSER_LOGFILE, "NULL");
        //Download the gecko driver
        WebDriverManager.firefoxdriver().setup();
        //Initialize the firefox driver
        WebDriver driver = new FirefoxDriver();

        driver.get("https://crontab.guru/");
        driver.manage().window().maximize();
        Thread.sleep(5000);
        driver.quit();

    }

   /* @Test(priority = 0)
    public void logoTest() {
        WebElement logo = driver.findElement(By.xpath("//body/div[@id='wrapper']/div[@id='content']/div[@id='divLogin']/div[@id='divLogo']/img[1]"));
        Assert.assertTrue(logo.isDisplayed(), "Message is not displayed");
    }

    @Test(priority = 1)
    public void titleTest() {
        String title = driver.getTitle();
        Assert.assertEquals(title,"OrangegRM", "Title is not matching");

    }


    @AfterClass
    void closeBrowser() {
        driver.quit();
    }*/
}
