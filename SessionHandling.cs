using System;  
using System.Web.UI;  
namespace SessionExample  
{  
    public partial class _Default : Page  
    {  
        protected void login_Click(object sender, EventArgs e)  
        {  
            if (password.Text=="qwe123")  
            {  
                // Storing email to Session variable  
                Session["email"] = email.Text;  
            }  
            // Checking Session variable is not empty  
            if (Session["email"] != null)  
            {  
                // Displaying stored email  
                Label3.Text = "This email is stored to the session.";  
                Label4.Text = Session["email"].ToString();  
            }  
        }  
    }  
}  
