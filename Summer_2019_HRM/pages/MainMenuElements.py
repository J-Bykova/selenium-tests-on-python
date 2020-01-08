
class MainMenuElements:

    def __init__(self, driver):

        self.driver = driver

        # Elements
        self.admin_menu = self.driver.find_element_by_id('menu_admin_viewAdminModule')
        self.pim_menu = self.driver.find_element_by_id('menu_pim_viewPimModule')
        self.leave_menu = self.driver.find_element_by_id('menu_leave_viewLeaveModule')
        self.time_menu = self.driver.find_element_by_id('menu_time_viewTimeModule')
        self.recruitment_menu = self.driver.find_element_by_id('menu_recruitment_viewRecruitmentModule')
        self.performance_menu = self.driver.find_element_by_id('menu__Performance')
        self.dashboard_menu = self.driver.find_element_by_id('menu_dashboard_index')


    def pushAdminMenu(self):
        self.admin_menu.click()

    def pushPimMenu(self):
        self.pim_menu.click()

    def pushLeaveMenu(self):
        self.leave_menu.click()

    def pushTimeMenu(self):
        self.time_menu.click()

    def pushRecruitmentMenu(self):
        self.recruitment_menu.click()

    def pushPerformanceMenu(self):
        self.performance_menu.click()

    def pushDashboardMenu(self):
        self.dashboard_menu.click()