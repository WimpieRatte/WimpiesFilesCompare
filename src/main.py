import os
import flet as ft


def main(page: ft.Page):

    #region Helper Functions
    def on_folder1_pick(event: ft.FilePickerResultEvent) -> None:
        # event.path holds the chosen directory when picking folders
        txtFolder1.value = event.path or ""
        txtFolder1.update()
    def on_folder2_pick(event: ft.FilePickerResultEvent) -> None:
        # event.path holds the chosen directory when picking folders
        txtFolder2.value = event.path or ""
        txtFolder2.update()

    def on_compare(_: ft.ControlEvent) -> None:
        loading_indicator.visible = True
        btnCompare.disabled = True
        loading_indicator.update()
        btnCompare.update()

        def finish() -> None:
            loading_indicator.visible = False
            btnCompare.disabled = False
            loading_indicator.update()
            btnCompare.update()

        try:
            folder1 = txtFolder1.value.strip()
            folder2 = txtFolder2.value.strip()

            if not folder1 or not folder2:
                message = "Select both folders before comparing."
                txtResults1.value = message
                txtResults2.value = message
                txtResults1.update()
                txtResults2.update()
                return

            if not os.path.isdir(folder1):
                txtResults1.value = f"Folder 1 not found: {folder1}"
                txtResults2.value = ""
                txtResults1.update()
                txtResults2.update()
                return

            if not os.path.isdir(folder2):
                txtResults1.value = ""
                txtResults2.value = f"Folder 2 not found: {folder2}"
                txtResults1.update()
                txtResults2.update()
                return

            files1 = {
                name
                for name in os.listdir(folder1)
                if os.path.isfile(os.path.join(folder1, name))
            }
            files2 = {
                name
                for name in os.listdir(folder2)
                if os.path.isfile(os.path.join(folder2, name))
            }

            only_in_1 = sorted(files1 - files2)
            only_in_2 = sorted(files2 - files1)

            txtResults1.value = "\n".join(only_in_1) if only_in_1 else "No unique files."
            txtResults2.value = "\n".join(only_in_2) if only_in_2 else "No unique files."
            txtResults1.update()
            txtResults2.update()
        finally:
            finish()
    #endregion

    #region Create Controls
    lblHeader = ft.Text("Folders compare", size=30, data=0)
    txtFolder1 = ft.TextField(label="Folder 1", expand=True)
    txtFolder2 = ft.TextField(label="Folder 2", expand=True)
    fpFolder1Picker = ft.FilePicker(on_result=on_folder1_pick)
    btnFolder1Picker = ft.IconButton(ft.Icons.FOLDER_OPEN, on_click=lambda _: fpFolder1Picker.get_directory_path())
    fpFolder2Picker = ft.FilePicker(on_result=on_folder2_pick)
    btnFolder2Picker = ft.IconButton(ft.Icons.FOLDER_OPEN, on_click=lambda _: fpFolder2Picker.get_directory_path())

    loading_indicator = ft.ProgressRing(visible=False)
    btnCompare = ft.ElevatedButton(text="Compare", on_click=on_compare)
    txtResults1 = ft.TextField(label="Files Only In Folder 1", multiline=True, expand=True)
    txtResults2 = ft.TextField(label="Files Only In Folder 2", multiline=True, expand=True)

    #endregion

    #region Add Controls
    page.overlay.append(fpFolder1Picker)
    page.overlay.append(fpFolder2Picker)
    page.add(
        # header label:
        ft.Container(
            lblHeader,
            alignment=ft.alignment.top_center,
        ),
        ft.Row(
            [
                ft.Container(
                    ft.Row([txtFolder1, btnFolder1Picker]),
                    expand=True
                ),
                ft.VerticalDivider(),
                ft.Container(
                    ft.Row([txtFolder2, btnFolder2Picker]),
                    expand=True
                ),
            ],
            spacing=0,
            height=50,
        ),
        ft.Row(
            [
                btnCompare,
                loading_indicator,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
        ),

        # Results:
        ft.Row(
            [
               ft.Container(
                    txtResults1,
                    alignment=ft.alignment.top_center,
                    expand=True
                ),
                ft.VerticalDivider(),
                ft.Container(
                    txtResults2,
                    alignment=ft.alignment.top_center,
                    expand=True
                ),
            ],
            spacing=0,
            expand=True
        )
    )
    #endregion


ft.app(main)
